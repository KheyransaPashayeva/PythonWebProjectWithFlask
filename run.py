from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes import *
from admin.routes import *
from models import *


if __name__ == '__main__':
    app.run(port=5000,debug=True)
