from flask import Flask
from products.routes import productos_bp
from clientes.routes import clientes_bp

from db import app

app.register_blueprint(productos_bp, url_prefix='/api/productos')
app.register_blueprint(clientes_bp, url_prefix='/api/clientes')

if __name__ == '__main__':
    app.run(debug=True)
