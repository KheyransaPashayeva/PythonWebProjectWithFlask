from flask import Flask,redirect,url_for,render_template,request
from app import app_bp
from app.forms import MessagesForm

@app_bp.route('/')
def app_index():
    from run import db
    from models import NavBar,Services,Testimonials,Transport,Feature,Faqs,Stats,SocialMedia,Pricing
    services=Services.query.all()
    context={
        "navbarlink":NavBar.query.all(),
        "services":services,
        "features":Feature.query.all(),
        "transports":Transport.query.all(),
        "testimonials":Testimonials.query.all(),
        "stats":Stats.query.all(),
        "faqs":Faqs.query.all(),
        "socialmedias":SocialMedia.query.all(),
        "pricings":Pricing.query.all()
    }
    return render_template('app/index.html',**context)

@app_bp.route('/contact', methods=['GET','POST'])
def app_contact():
    from run import db
    from models import NavBar,Messages,SocialMedia
    navbarlink=NavBar.query.all()
    messagesForm=MessagesForm()
    socialmedias=SocialMedia.query.all()
    if request.method=="POST":
        message=Messages(
            name=messagesForm.name.data,
            email=messagesForm.email.data,
            subject=messagesForm.subject.data,
            message=messagesForm.message.data,
            message_date=messagesForm.message_date.data
        )
        db.session.add(message)
        db.session.commit()
        return redirect('/contact')
        
    return render_template('app/contact.html',navbarlink=navbarlink,messagesForm=messagesForm,socialmedias=socialmedias)

@app_bp.route('/about')
def app_about():
    from run import db
    from models import NavBar,Team,Testimonials,Stats,Faqs,SocialMedia,TeamSocial
    context={
    "teamsocials":TeamSocial.query.all(),
    "navbarlink":NavBar.query.all(),
    "teams":Team.query.all(),
    "testimonials":Testimonials.query.all(),
    "stats":Stats.query.all(),
    "faqs":Faqs.query.all(),
    "socialmedias":SocialMedia.query.all()
    }
    return render_template('app/about.html',**context)

@app_bp.route('/service')
def app_service():
    from run import db
    from models import NavBar,Services,Testimonials,Feature,Transport,Faqs,SocialMedia
    services=Services.query.all()
    context={
        "navbarlink":NavBar.query.all(),
        "services":services,
        "features":Feature.query.all(),
        "testimonials":Testimonials.query.all(),
        "transports":Transport.query.all(),
        "faqs":Faqs.query.all(),
        "socialmedias":SocialMedia.query.all()  
    }
    return render_template('app/services.html',**context)

@app_bp.route('/service-detail/<int:id>', methods=['GET','POST'])
def app_service_detail(id):
    from run import db
    from models import Services,NavBar,SocialMedia

    context={
        "navbarlink":NavBar.query.all(),
        "services":Services.query.get(id),
        "service":Services.query.all(),
        "socialmedias":SocialMedia.query.all()
    }
    return render_template('app/service-details.html',**context)

