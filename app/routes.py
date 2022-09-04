from flask import Flask,redirect,url_for,render_template,request
from app import app_bp

@app_bp.route('/')
def app_index():
    from run import db
    from models import NavBar,Services
    navbarlink=NavBar.query.all()
    services=Services.query.all()
    return render_template('app/index.html',navbarlink=navbarlink,services=services)

@app_bp.route('/contact')
def app_contact():
    from run import db
    from models import NavBar
    navbarlink=NavBar.query.all()
    return render_template('app/contact.html',navbarlink=navbarlink)

@app_bp.route('/about')
def app_about():
    from run import db
    from models import NavBar
    navbarlink=NavBar.query.all()
    return render_template('app/about.html',navbarlink=navbarlink)

@app_bp.route('/service')
def app_service():
    from run import db
    from models import NavBar,Services
    navbarlink=NavBar.query.all()
    services=Services.query.all()
    return render_template('app/services.html',navbarlink=navbarlink,services=services)

@app_bp.route('/service_detail/<int:id>',methods=['GET','POSt'])
def app_service_detail(id):
    from run import db
    from models import NavBar,Services
    navbarlink=NavBar.query.all()
    services=Services.query.get(id)
    return render_template('app/service-detail.html',navbarlink=navbarlink,services=services)

@app_bp.route('/pricing')
def app_pricing():
    from run import db
    from models import NavBar
    navbarlink=NavBar.query.all()
    return render_template('app/pricing.html',navbarlink=navbarlink)