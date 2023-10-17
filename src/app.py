from flask import Flask
from products.routes import productos_bp
from ventas.routes import ventas_bp
from db import app

app.register_blueprint(productos_bp, url_prefix='/api/productos')
app.register_blueprint(ventas_bp, url_prefix='/api/ventas')

if __name__ == '__main__':
    app.run(debug=True)
