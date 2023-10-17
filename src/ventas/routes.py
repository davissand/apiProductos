from flask import Blueprint, jsonify, request

from db import mysql

ventas_bp = Blueprint('ventas', __name__)

@ventas_bp.route('/ventas', methods=['GET'])
def get_ventas():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM venta")
        #cursor.execute("SELECT p.nombre, p.precio, c.nombre FROM producto as p INNER JOIN categoria_producto as c ON p.categoria_id = c.id")
        ventas = cursor.fetchall()        
        cursor.close()
        return jsonify(ventas)
    except Exception as e:
        print(e)
        return jsonify(error=str(e))