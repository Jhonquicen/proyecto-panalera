from flask import render_template, jsonify, redirect, session, request, flash
from flask_app import app

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.pedidos import Pedido
from flask_app.models.productos import Producto
from flask_app.models.producto_del_pedido import Productopedido

from datetime import datetime

@app.route('/factura/pedido')
def factura_pedido():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    #La instancia del producto que queremos editar
    formulario_registro = {"id": id}
    producto = Producto.get_by_id(formulario_registro) #para enviar el formulario
    pedido = Pedido.get_by_id(formulario_registro )
    productopedido = Productopedido.get_by_id(formulario_registro)

    return render_template('factura_pedido.html', user=user, producto=producto, pedido=pedido, productopedido=productopedido)



@app.route('/new/pedido')
def new_pedido():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)
    pedido = Pedido.get_all()


    return render_template('new_pedido.html', user=user, pedido=pedido) #para mandar la validacion de la creacion del pedido



@app.route('/create/pedido', methods=['POST'])
def create_pedido():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    if not Pedido.valida_pedido(request.form): #llama a la función de valida_pedido(pedidos.py) enviándole el formulario, comprueba que sea valido 
        return redirect('/new/pedido')

    Pedido.save(request.form)

    return redirect('/pedidos') #para mandar la validacion de la creacion del pedido


@app.route('/edit/pedido/<int:id>') #a través de la URL recibimos el ID de la pedido
def edit_pedido(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    #La instancia del pedido que queremos editar
    formulario_pedido = {"id": id}
    pedido = Pedido.get_by_id(formulario_pedido) #formulario_pedido(nombre de la validacion en este caso pedido, para hacer el jinja)
    fecha=datetime.today().strftime('%Y-%m-%d')
    print(fecha)
    return render_template('edit_pedido.html', user=user, pedido=pedido, fecha=fecha)

@app.route('/update/pedido', methods=['POST'])
def update_pedido():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')
    
    if not Pedido.valida_pedido(request.form): #llama a la función de valida_pedido enviándole el formulario, comprueba que sea valido 

        return redirect('/edit/pedido/'+request.form['id'])

    
    Pedido.update(request.form)
    return redirect('/pedidos')



@app.route('/delete/pedido/<int:id>')
def delete_pedido(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {"id": id}

    Productopedido.delete_by_Id(formulario)
    Pedido.delete(formulario)
    
    return redirect('/pedidos')


