from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.api.auth import *
from app.routes import *