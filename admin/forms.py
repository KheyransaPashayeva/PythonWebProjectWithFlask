from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,DateField,PasswordField,SubmitField,TextAreaField,IntegerField,BooleanField

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
    
class NavbarLinkForm(FlaskForm):
    navbar_name=StringField('NavlinkrName')
    navbar_url=StringField('NavlinkUrl')
    navbar_order=IntegerField('NavlinkOrder')
    is_active=BooleanField('Is Active')
    submit=SubmitField('Add navlink')