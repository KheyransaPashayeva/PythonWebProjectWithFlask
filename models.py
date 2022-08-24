from run import app,db

#contactdan geden msjlar
class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120),nullable=False)
    message = db.Column(db.String(220),nullable=False)
    
#saytin Navbar hissesi
class NavBar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    navbar_name = db.Column(db.String(180), unique=True, nullable=False)
    navbar_url = db.Column(db.String(180), unique=True, nullable=False)
    
class Transport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transport_title = db.Column(db.String(180), unique=True, nullable=False)
    transport_text = db.Column(db.String(220), unique=True, nullable=False)
    transport_img = db.Column(db.String(120), nullable=False)
    
class AboutUs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about_title = db.Column(db.String(180), unique=True, nullable=False)
    about_text = db.Column(db.String(220), unique=True, nullable=False)
    about_video = db.Column(db.String(120), nullable=False)
    

    
class AboutIcon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about_icon_title = db.Column(db.String(180), unique=True, nullable=False)
    about_icon_text = db.Column(db.String(220), unique=True, nullable=False)
    about_icon_img = db.Column(db.String(120), nullable=False)
    
    
class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_title = db.Column(db.String(180), unique=True, nullable=False)
    service_text = db.Column(db.String(220), unique=True, nullable=False)
    service_img = db.Column(db.String(120), nullable=False)
    