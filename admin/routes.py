from flask import Flask,redirect,url_for,render_template,request
from admin import admin_bp
from admin.forms import MessagesForm

@admin_bp.route('/')
def admin_index():
    return render_template('admin/index.html')

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
    return render_template('admin/message_create.html',messageForm=messageForm)