from flask import Blueprint, jsonify, request
from db import mysql

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/productos', methods=['GET'])
def get_productos():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM producto")
        #cursor.execute("SELECT p.nombre, p.precio, c.nombre FROM producto as p INNER JOIN categoria_producto as c ON p.categoria_id = c.id")
        productos = cursor.fetchall()        
        cursor.close()
        return jsonify(productos)
    except Exception as e:
        print(e)
        return jsonify(error=str(e))
    
@productos_bp.route('/prod_cat', methods=['GET'])
def prod_cat():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT p.nombre, p.precio, c.nombre FROM producto as p INNER JOIN categoria_producto as c ON p.categoria_id = c.id")
        productos = cursor.fetchall()        
        cursor.close()
        return jsonify(productos)
    except Exception as e:
        print(e)
        return jsonify(error=str(e))

@productos_bp.route('/detalle/<id>', methods=['GET'])
def detalle(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM producto WHERE id = %s", (id,))
        producto = cursor.fetchone()
        cursor.close()
        if producto != None:
            detalle = {'id': producto[0], 'nombre': producto[1],'precio': producto[2], 'categoria_id':producto[3]}
            return jsonify(detalle)
        else:
            return jsonify({'mensaje':'producto no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje':'Error'})
    

@productos_bp.route('/productos', methods=['POST'])
def insertar_producto():
    try:
        # Obtén los datos del producto desde la solicitud
        datos_producto = request.get_json()

        # Extrae los datos del JSON
        nombre = datos_producto['nombre']
        precio = datos_producto['precio']
        categoria_id = datos_producto['categoria_id']

        # Realiza la inserción en la base de datos
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO producto (nombre, precio, categoria_id) VALUES (%s, %s, %s)", (nombre, precio, categoria_id))
        mysql.connection.commit()
        cursor.close()

        # Devuelve una respuesta exitosa
        return jsonify(message="Producto insertado correctamente"), 201
    except Exception as e:
        # En caso de error, devuelve un mensaje de error
        print(e)
        return jsonify(error="Error al insertar el producto"), 500

# Ruta para actualizar un producto por su ID
@productos_bp.route('/productos/<id>', methods=['PUT'])
def actualizar_producto(id):
    try:
        # Obtén los datos del producto desde la solicitud
        datos_producto = request.get_json()

        # Extrae los datos del JSON
        nombre = datos_producto.get('nombre')
        precio = datos_producto.get('precio')
        categoria_id = datos_producto.get('categoria_id')

        # Actualiza el producto en la base de datos
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE producto SET nombre=%s, precio=%s, categoria_id=%s WHERE id=%s", (nombre, precio, categoria_id, id))
        mysql.connection.commit()
        cursor.close()

        # Devuelve una respuesta exitosa
        return jsonify(message="Producto actualizado correctamente"), 200
    except Exception as e:
        # En caso de error, devuelve un mensaje de error
        print(e)
        return jsonify(error="Error al actualizar el producto"), 500

# Ruta para eliminar un producto por su ID
@productos_bp.route('/productos/<id>', methods=['DELETE'])
def eliminar_producto(id):
    try:
        # Elimina el producto de la base de datos
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM producto WHERE id=%s", (id,))
        mysql.connection.commit()
        cursor.close()

        # Devuelve una respuesta exitosa
        return jsonify(message="Producto eliminado correctamente"), 200
    except Exception as e:
        # En caso de error, devuelve un mensaje de error
        print(e)
        return jsonify(error="Error al eliminar el producto"), 500