from flask import Flask,redirect,url_for,render_template,request
from admin import admin_bp
from admin.forms import MessagesForm,ServiceForm

@admin_bp.route('/')
def admin_index():
    return render_template('admin/dashboard.html')

@admin_bp.route('/message/create',methods=['GET','POST'])
def admin_message_create():
    messageForm=MessagesForm()
    from run import db
    from models import Messages
    if request.method=='POST':
        message=Messages(
            name=messagesForm.name.data,
            email=messageForm.email.data,
            subject=messageForm.subject.data,
            message=messageForm.message.data,
            message_date=messageForm.message_date.data
        )
        db.session.add(message)
        db.session.commit()
        return redirect('/message/create')
    return render_template('admin/message_create.html',messageForm=messageForm)


@admin_bp.route('/service',methods=['GET','POST'])
def admin_service_create():
    serviceForm=ServiceForm()
    from run import db
    from models import Services
    services=Services.query.all()
    if request.method=='POST':
        service_title=serviceForm.service_title.data
        service_img=serviceForm.service_img.data
        service_text=serviceForm.service_text.data
        service=Services(service_title=service_title,service_img=service_img,service_text=service_text )
        db.session.add(service)
        db.session.commit()
    return render_template('admin/blank.html',serviceForm=serviceForm,services=services)