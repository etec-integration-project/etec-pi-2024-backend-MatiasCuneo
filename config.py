import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

host = os.getenv('HOST')

app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://root:root@{host}:5432/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)