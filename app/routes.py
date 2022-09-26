from flask import Flask,redirect,url_for,render_template,request
from app import app_bp

@app_bp.route('/')
def app_index():
    from run import db
    from models import NavBar,Services,Testimonials,Transport,Feature,Faqs
    navbarlink=NavBar.query.all()
    services=Services.query.all()
    testimonials=Testimonials.query.all()
    transports=Transport.query.all()
    features=Feature.query.all()
    faqs=Faqs.query.all()
    return render_template('app/index.html',navbarlink=navbarlink,services=services,testimonials=testimonials,transports=transports,features=features,faqs=faqs)

@app_bp.route('/contact')
def app_contact():
    from run import db
    from models import NavBar
    navbarlink=NavBar.query.all()
    return render_template('app/contact.html',navbarlink=navbarlink)

@app_bp.route('/about')
def app_about():
    from run import db
    from models import NavBar,Team,Testimonials
    navbarlink=NavBar.query.all()
    teams=Team.query.all()
    testimonials=Testimonials.query.all()
    return render_template('app/about.html',navbarlink=navbarlink,teams=teams,testimonials=testimonials)

@app_bp.route('/service')
def app_service():
    from run import db
    from models import NavBar,Services,Testimonials,Feature,Transport,Faqs
    navbarlink=NavBar.query.all()
    services=Services.query.all()
    features=Feature.query.all()
    testimonials=Testimonials.query.all()
    transports=Transport.query.all()
    faqs=Faqs.query.all()
    return render_template('app/services.html',navbarlink=navbarlink,services=services,features=features,testimonials=testimonials,transports=transports,faqs=faqs)

@app_bp.route('/service-detail/<int:id>', methods=['GET','POST'])
def app_service_detail(id):
    from run import db
    from models import Services,NavBar
    navbarlink=NavBar.query.all()
    services=Services.query.get(id)
    return render_template('app/service-details.html',navbarlink=navbarlink,services=services)

