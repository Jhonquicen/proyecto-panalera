from flask_app.config.mysqlconnection import  connectToMySQL



import re #Importando Expresiones regulares
#Expresion Regular de Email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash

class Producto:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.imagen = data['imagen']
        self.descripcion = data['descripcion']
        self.precio = data['precio']
        self.inventario = data['inventario']
        self.categoria = data['categoria']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO productos (name, imagen, descripcion, precio, inventario, categoria) VALUES (%(name)s, %(imagen)s, %(descripcion)s, %(precio)s, %(inventario)s, %(categoria)s) "
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario)
        return result

    @staticmethod
    def valida_producto(formulario):
        es_valido = True    
        
        if len(formulario['name']) < 3:
            flash('el nombre debe tener al menos 3 caracteres', 'producto')
            es_valido = False

        

        if len(formulario['descripcion']) < 3:
            flash('la descripcion debe tener al menos 3 caracteres', 'producto')
            es_valido = False

        if len(formulario['precio']) < 3:
            flash('el precio debe tener al menos 3', 'producto')
            es_valido = False

        return es_valido


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM proyecto_pañalera.productos;" 
        results = connectToMySQL('proyecto_pañalera').query_db(query) #Lista de diccionarios 
        productos = []
        for producto in results:
            #producto = diccionario
            productos.append(cls(producto))

        return productos

    @classmethod
    def categorias(cls, formulario):
        query = "SELECT * FROM productos WHERE categoria = %(categoria)s"
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario)
        print(result)
        producto= cls(result[0]) #creamos una instancia de producto
        return producto

    @classmethod
    def producto(cls, formulario):
        query = "SELECT * FROM productos WHERE id = %(id)s"
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario)
        print(result)
        producto= cls(result[0]) #creamos una instancia de producto
        return producto

    @classmethod
    def ropa(cls):
        query = "SELECT * FROM productos WHERE categoria LIKE 'ropa'"
        results = connectToMySQL('proyecto_pañalera').query_db(query) #Lista de diccionarios 
        productos = []
        for producto in results:
            #producto = diccionario
            productos.append(cls(producto))

        return productos

    @classmethod
    def accesorios(cls):
        query = "SELECT * FROM productos WHERE categoria LIKE 'accesorios'"
        results = connectToMySQL('proyecto_pañalera').query_db(query) #Lista de diccionarios 
        productos = []
        for producto in results:
            #producto = diccionario
            productos.append(cls(producto))

        return productos

    @classmethod
    def get_by_id(cls, formulario): #formulario = {id: 1}, recibe el formulario = id
        query = "SELECT * FROM productos WHERE id = %(id)s"
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario) #RECIBIMOS UNA LISTA
        print(result)
        producto = cls(result[0]) #creamos una instancia de producto
        return producto

    

    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de producto a borrar
        query = "DELETE FROM productos WHERE id = %(id)s"
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario)
        return result


    # @classmethod
    # def carrito(cls):
    #     query = "SELECT * FROM productos WHERE id = %(id)s"
    #     result = connectToMySQL('proyecto_pañalera').query_db(query)
    #     return result

    