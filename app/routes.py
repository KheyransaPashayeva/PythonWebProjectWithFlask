from flask import Flask,redirect,url_for,render_template,request
from app import app_bp

@app_bp.route('/')
def app_index():
    from run import db
    from models import NavBar,Services,Testimonials,Transport,Feature,Faqs,Stats
    context={
        "navbarlink":NavBar.query.all(),
        "services":Services.query.all(),
        "features":Feature.query.all(),
        "transports":Transport.query.all(),
        "testimonials":Testimonials.query.all(),
        "stats":Stats.query.all(),
        "faqs":Faqs.query.all()
    }
    return render_template('app/index.html',**context)

@app_bp.route('/contact')
def app_contact():
    from run import db
    from models import NavBar
    navbarlink=NavBar.query.all()
    return render_template('app/contact.html',navbarlink=navbarlink)

@app_bp.route('/about')
def app_about():
    from run import db
    from models import NavBar,Team,Testimonials,Stats,Faqs
    context={
    "navbarlink":NavBar.query.all(),
    "teams":Team.query.all(),
    "testimonials":Testimonials.query.all(),
    "stats":Stats.query.all(),
    "faqs":Faqs.query.all()
    }
    return render_template('app/about.html',**context)

@app_bp.route('/service')
def app_service():
    from run import db
    from models import NavBar,Services,Testimonials,Feature,Transport,Faqs
    context={
        "navbarlink":NavBar.query.all(),
        "services":Services.query.all(),
        "features":Feature.query.all(),
        "testimonials":Testimonials.query.all(),
        "transports":Transport.query.all(),
        "faqs":Faqs.query.all()  
    }
    return render_template('app/services.html',**context)

@app_bp.route('/service-detail/<int:id>', methods=['GET','POST'])
def app_service_detail(id):
    from run import db
    from models import Services,NavBar
    context={
        "navbarlink":NavBar.query.all(),
        "services":Services.query.get(id)
    }
    return render_template('app/service-details.html',**context)

