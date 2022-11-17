from flask_app.config.mysqlconnection import  connectToMySQL

from flask import flash

class Productopedido:
    def __init__(self, data):
        self.pedido_id = data['pedido_id']
        self.producto_id = data['producto_id']
        self.cantidad = data['cantidad']


    
    @classmethod 
    def save(cls, formulario):
        
        query = "INSERT INTO productos_del_pedido (pedido_id, producto_id, cantidad) VALUES (%(pedido_id)s, %(producto_id)s, %(cantidad)s) "
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario)
    
        return result

    @classmethod
    def delete_by_Id(cls, formulario): #Recibe formulario con id de receta a borrar
        query = "DELETE FROM productos_del_pedido WHERE pedido_id = %(id)s"
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de receta a borrar
        query = "DELETE FROM productos_del_pedido WHERE pedido_id = %(id)s"
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls, formulario):
        query = "SELECT * FROM productos INNER JOIN productos_del_pedido ON producto_id = productos.id INNER JOIN pedidos ON pedido_id = pedidos.id WHERE pedidos.id = %(id)s ;"
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario)
        productopedido = []
        for pr in result:
            #pedido = diccionario
            productopedido.append(cls(pr)) 

        return productopedido



    @classmethod
    def get_by_id(cls, formulario): #formulario = {id: 1}, recibe el formulario = id
        query = "SELECT * FROM productos_del_pedido WHERE pedido_id = %(id)s"
        result = connectToMySQL('proyecto_pañalera').query_db(query, formulario) #RECIBIMOS UNA LISTA
        print(result)

        productopedido = cls(result[0]) #creamos una instancia de producto
        return productopedido



    @classmethod
    def carrito(cls):
        query = "INSERT INTO productos_del_pedido (pedido_id, producto_id, cantidad) VALUES (%(pedido_id)s, %(producto_id)s, %(cantidad)s)"
        result = connectToMySQL('proyecto_pañalera').query_db(query)
        return result


    