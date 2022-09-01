from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

main=Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
main.config['SECRET_KEY']="secretkey"
db=SQLAlchemy(main)
migrate=Migrate(main, db)
from app import app_bp
from admin import admin_bp

main.register_blueprint(app_bp)
main.register_blueprint(admin_bp)

from app.routes import *
from admin.routes import *
from models import *



if __name__ == '__main__':
    main.run(port=5000,debug=True)
