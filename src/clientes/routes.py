from flask import Blueprint, jsonify, request

from db import mysql

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/clientes', methods=['GET'])
def get_clientes():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM cliente")
        #cursor.execute("SELECT p.nombre, p.precio, c.nombre FROM producto as p INNER JOIN categoria_producto as c ON p.categoria_id = c.id")
        clientes = cursor.fetchall()        
        cursor.close()
        
        return jsonify(clientes)
    except Exception as e:
        print(e)
        return jsonify(error=str(e))