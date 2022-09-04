from run import main,db
import datetime

#contactdan geden msjlar
class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120))
    message = db.Column(db.Text(220))
    message_date = db.Column(db.String(120))
    
#saytin Navbar hissesi
class NavBar(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    navbar_name = db.Column(db.String(180), unique=True, nullable=False)
    navbar_url = db.Column(db.String(180), unique=True, nullable=False)
    navbar_order=db.Column(db.Integer,unique=True)
    is_active = db.Column(db.Boolean)
    
class Transport(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    transport_title = db.Column(db.String(180), unique=True, nullable=False)
    transport_text = db.Column(db.String(220), nullable=False)
    transport_img = db.Column(db.String(120), nullable=False)
    
class AboutUs(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    about_title = db.Column(db.String(180), unique=True, nullable=False)
    about_text = db.Column(db.String(220))
    about_video = db.Column(db.String(120))
    

    
class AboutIcon(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    about_icon_title = db.Column(db.String(180), unique=True, nullable=False)
    about_icon_text = db.Column(db.String(220))
    about_icon_img = db.Column(db.String(120))
    
    
class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    service_title = db.Column(db.String(180), unique=True, nullable=False)
    service_text = db.Column(db.Text)
    service_img = db.Column(db.String(120))
    
    
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    user_email = db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean)