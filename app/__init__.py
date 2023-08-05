import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

if not os.getenv('SECRET_KEY'):
    print('NO SECRET KEY SET!')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'you-will-never-guess'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
