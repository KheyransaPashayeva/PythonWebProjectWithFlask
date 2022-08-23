from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
db = SQLAlchemy(app)
from models import *
from routes.contact import *

# @app.route('/')
# def home():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)
