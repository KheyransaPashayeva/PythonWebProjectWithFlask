from flask import Flask,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

main=Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
main.config['SECRET_KEY']="secretkey"
UPLOAD_FOLDER = './static/uploads/'
main.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
main.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  #1mb limiti tetbiq edirik
db=SQLAlchemy(main)
migrate=Migrate(main, db)
login_manager=LoginManager(main)

@login_manager.user_loader
def load_user(user_id):
    from models import Users
    return Users.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.auth_login'))

#import blueprint app
from app import app_bp
from admin import admin_bp
from auth import auth_bp

#register app
main.register_blueprint(app_bp)
main.register_blueprint(admin_bp)
main.register_blueprint(auth_bp)

#import routes
from app.routes import *
from admin.routes import *
from auth.routes import *
from models import *
# db.create_all()


if __name__ == '__main__':
    main.run(port=5000,debug=True)


