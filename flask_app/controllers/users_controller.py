from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.pedidos import Pedido
from flask_app.models.productos import Producto
from flask_app.models.producto_del_pedido import Productopedido

#Importación BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

    

@app.route('/registrate', methods=['POST'])
def registrate():
    #Validar la información ingresada
    if not User.valida_usuario(request.form):
        return redirect('/')

    pwd = bcrypt.generate_password_hash(request.form['password']) #Encriptamos el password del usuario

    formulario = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pwd
    }

    #request.form = FORMULARIO HTML
    id = User.save(formulario) #Recibo el identificador de mi nuevo usuario

    session['user_id'] = id

    return redirect('/pedidos')

@app.route('/login', methods=['POST'])
def login():
    #Verificar que el email EXISTA
    #request.form RECIBIMOS DE HTML
    #request.form = {email: elena@cd.com, password: 123}
    user = User.get_by_email(request.form) #Recibiendo una instancia de usuario o Falso

    if not user:
        #flash('E-mail no encontrado', 'login')
        #return redirect('/')
        return jsonify(message="E-mail no encontrado")

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        #flash('Password incorrecto', 'login')
        #return redirect('/')
        return jsonify(message="Password no encontrado")
    
    session['user_id'] = user.id
    return redirect('/pedidos')
    #return redirect('/dashboard')
    return jsonify(message="correcto")

    

@app.route('/pedidos')
def pedidos():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)

    pedidos = Pedido.get_all()
    productos = Producto.get_all()

    return render_template('pedidos.html', user=user, pedidos=pedidos, productos=productos) #carga la plantilla


@app.route('/administrador')
def productos():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)

    productos = Producto.get_all()
    

    return render_template('administrador.html', user=user, productos=productos) #carga la plantilla



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/administrador')
def administrador():
    if 'user_id' not in session:
        return redirect('/')

    return render_template('/administrador.html')