from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'productos'
app.config['JSON_AS_ASCII'] = False

mysql = MySQL(app)
