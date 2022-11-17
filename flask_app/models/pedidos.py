from flask_app.config.mysqlconnection import  connectToMySQL

import re #Importando Expresiones regulares
#Expresion Regular de Email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash

class Pedido:

    def __init__(self, data):
        self.id = data['id']
        self.fecha = data['fecha']
        self.direccion = data['direccion']
        self.subtotal = data['subtotal']
        self.iva = data['iva']
        self.total = data['total']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        #LEFT JOIN para obtener el nombre que hace el pedido
        

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO pedidos (fecha, direccion, subtotal, iva, total, user_id) VALUES (%(fecha)s, %(direccion)s, %(subtotal)s, %(iva)s, %(total)s, %(user_id)s) "
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario)
        return result

    @staticmethod
    def valida_pedido(formulario):
        es_valido = True    
        

        if formulario['fecha'] == "":
            flash('Ingrese una fecha', 'pedido')
            es_valido = False
        

        if len(formulario['direccion']) < 1:
            flash('el pedido debe tener al menos un seleccion', 'pedido')
            es_valido = False

        
        
        return es_valido

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM proyecto_pañalera.pedidos;"
        results = connectToMySQL('proyecto_pañalera').query_db(query) #Lista de diccionarios 
        pedidos = []
        for pedido in results:
            #pedido = diccionario
            pedidos.append(cls(pedido)) #1.- cls(pedido) me crea una instancia en base al diccionario, 2.- Agrego la instancia a mi lista de proyecto_pañalera

        return pedidos

    @classmethod
    def get_by_id(cls, formulario): #formulario = {id: 1}
        query = "SELECT pedidos.* FROM pedidos LEFT JOIN users ON users.id = pedidos.user_id WHERE pedidos.id = %(id)s"
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario) # nos devuelve una Lista de diccionarios
        pedido = cls(result[0])
        return pedido

    @classmethod 
    def update(cls, formulario):
        query = "UPDATE pedidos SET direccion=%(direccion)s, fecha=%(fecha)s WHERE id = %(id)s"
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de pedido a borrar
        query = "DELETE FROM pedidos WHERE id = %(id)s"
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario)
        return result
    

    