from flask_mysqldb import MySQL
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'productos'
app.config['JSON_AS_ASCII'] = False

mysql = MySQL(app)
