

from flask import render_template, redirect, session, jsonify,request, flash
from flask_app import app

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.productos import Producto
from flask_app.models.pedidos import Pedido
from datetime import datetime
from werkzeug.utils import secure_filename
import os





@app.route('/proceso', methods=['POST'])
def proceso():
    #para guardar en session
    session['precios'] = request.form['factura'] #el nombre del request.form debe ser igual al "name" del html
    return redirect('factura_pedido.html')

@app.route("/crear/producto", methods=['POST'])
def crear_producto():
    if not Producto.valida_producto(request.form): #llama a la función de valida_pedido(pedidos.py) enviándole el formulario, comprueba que sea valido 
        return redirect('/new/pedido')

    image = request.files["imagen"]
    img_name = "products/"+secure_filename(image.filename).split(".")[0]+str(datetime.now()).replace(" ","_").replace(":","_").replace(".","_")+"."+secure_filename(image.filename).split(".")[1]
    path=os.path.join(app.config['UPLOAD_FOLDER'], img_name)
    print(path)
    image.save(path)

    formulario = {
        "name": request.form["name"],
        "imagen": img_name,
        "descripcion": request.form['descripcion'],
        "precio": request.form['precio'],
        "inventario": request.form['inventario'],
        "categoria": request.form['categoria'],
    }
    producto = Producto.save(formulario)
    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión
    

    return render_template('administrador.html', user=user, producto=producto)
    

@app.route('/carrito', methods=['POST'])
def carrito():


    if "carrito" not in session:
        session["carrito"]={}
    
    productos_id = request.form["id"]# recibo el "id" de mi formulario
    if productos_id not in session["carrito"]: #se guarda en carrito
        session["carrito"][productos_id]=1
    else:
        session["carrito"][productos_id]+=1
    session.modified = True # para actualizar y guardar el valor siempre importante
    
    print(session["carrito"])
    return redirect('/checkout')




@app.route('/ropa')
def ropa_catalogo():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)   
    productos = Producto.ropa()
    print(productos)

    return render_template('ropa.html', user=user, productos=productos)



@app.route('/accesorios')
def accesorios_catalogo():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)
    productos = Producto.accesorios() 

    return render_template('accesorios.html', user=user, productos=productos)

