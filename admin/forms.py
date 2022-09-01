from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,DateField,PasswordField,SubmitField,TextAreaField

class MessagesForm(FlaskForm):
    name=StringField('Name')
    email=EmailField('Email')
    subject=StringField('Subject')
    message=TextAreaField('Message')
    message_date=DateField('message_date')
    submit=SubmitField('Add message')

class ServiceForm(FlaskForm):
    service_title=StringField('ServiceTitle')
    service_img=StringField('ServiceIMG')
    service_text=TextAreaField('ServiceText')
    submit=SubmitField('Add service')