
from flask import render_template, jsonify, redirect, session, request, flash
from flask_app import app

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.pedidos import Pedido
from flask_app.models.productos import Producto
from flask_app.models.producto_del_pedido import Productopedido


@app.route('/checkout')
def checkout():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    if "carrito" not in session:
        session["carrito"]={}

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) 

    productos = []
    
    cantidades = []
    subtotal = 0
    iva = 19
    total = 0
    print(session)
    for x in session['carrito']:
        cantidades.append(session['carrito'][x])
        
        formulario={
            "id": x
        }

        producto = Producto.get_by_id(formulario)
        
        total += int(producto.precio) * session['carrito'][x] 
        productos.append(producto)
        
    iva = int(total  * 0.19)
    subtotal = total - iva
    print(productos)
    print(cantidades)
    print(total)
    print(iva)
    return render_template('checkout.html', user=user, productos=productos, cantidades=cantidades, subtotal=subtotal, iva=iva, total=total)


@app.route('/delete_checkout/<id>') #a través de la URL recibimos el ID de la receta
def delete_checkout(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')


    del session['carrito'][id]
    session.modified = True 

    return redirect('/checkout')

@app.route('/sumar/checkout', methods=['POST'])
def sumar_checkout():

    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    if "carrito" not in session:
        session["carrito"]={}
    print(request.form)
    producto = request.form["id"]# recibo el "id" de mi formulario
    if producto not in session["carrito"]: #se guarda en carrito
        session["carrito"][producto]=1
    else:
        session["carrito"][producto]+=1
    session.modified = True # para actualizar y guardar el valor siempre importante
    print(session["carrito"])
    return redirect('/checkout')

@app.route('/restar/checkout', methods=['POST'])
def restar_checkout():

    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    if "carrito" not in session:
        session["carrito"]={}
    print(request.form)
    producto = request.form["id"]# recibo el "id" de mi formulario
    if producto not in session["carrito"]: #se guarda en carrito
        session["carrito"][producto]=1
    else:
        session["carrito"][producto]-=1
    session.modified = True # para actualizar y guardar el valor siempre importante
    print(session["carrito"])
    return redirect('/checkout')


@app.route('/ingresar/factura', methods=['POST'])
def ingresar_factura():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    print(request.form)
    id_pedido=Pedido.save(request.form)
    print(id_pedido)
    
    for key in session['carrito']:
        formulario = {
            "pedido_id": id_pedido, 
            "producto_id": key,
            "cantidad": session['carrito'][key]
        }
        Productopedido.save(formulario)
        print(key)
        print(session['carrito'][key])

    

    formulario = {
        'id': session['user_id']
    }
    productopedido = Productopedido.get_all(formulario)
    
    

    print(productopedido)

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    return redirect('/pedidos')


