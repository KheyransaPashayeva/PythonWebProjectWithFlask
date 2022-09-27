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
    transport_text = db.Column(db.String(220))
    transport_img = db.Column(db.String(120))
    transport_url = db.Column(db.String(120))
    
class AboutUs(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    about_title = db.Column(db.String(180), unique=True, nullable=False)
    about_text = db.Column(db.String(220))
    about_video = db.Column(db.String(120))
    
class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name=db.Column(db.String(220))
    value=db.Column(db.Integer)
    
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(180), nullable=False)
    employee_img = db.Column(db.String(220))
    position = db.Column(db.String(120))  
    info= db.Column(db.Text)
    order=db.Column(db.Integer)
    is_active=db.Column(db.Boolean)
    extra_img=db.relationship('TeamGallery', backref='team', lazy=True)
    
class TeamGallery(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    teamgallery_id=db.Column(db.Integer,db.ForeignKey('team.id'))
    img=db.Column(db.String(80))
    
class Testimonials(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(80))
    profession=db.Column(db.String(80))
    info=db.Column(db.Text)
    img=db.Column(db.String(80))
    order=db.Column(db.Integer)
    isActive=db.Column(db.Boolean)

    
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
    user_info =db.Column(db.Text)
   
    
class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    feature_title = db.Column(db.String(180))
    feature_img = db.Column(db.String(120))
    feature_text =db.Column(db.Text)
    feature_orderimg=db.Column(db.String(80))
    feature_ordertext=db.Column(db.String(80))
    is_active = db.Column(db.Boolean)
    
class Faqs(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    faq_question = db.Column(db.String(220))
    faq_answer = db.Column(db.String(220))