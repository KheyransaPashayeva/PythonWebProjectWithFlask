from flask import Flask
main=Flask(__name__)
from app.routes import *
from admin.routes import *


from app import app_bp
from admin import admin_bp

main.register_blueprint(app_bp)
main.register_blueprint(admin_bp)

if __name__ == '__main__':
    main.run(port=5000,debug=True)
