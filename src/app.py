from flask import Flask
from products.routes import productos_bp
from db import app

app.register_blueprint(productos_bp, url_prefix='/api/productos')

if __name__ == '__main__':
    app.run(debug=True)
