from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,DateField,PasswordField,SubmitField,TextAreaField,IntegerField,BooleanField,FileField

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
    
class TeamForm(FlaskForm):
    name=StringField('Employee Name')
    employee_img=FileField('Employee Image')
    position=StringField('Position')
    info=TextAreaField('Info')
    order=IntegerField('Order')
    is_active=BooleanField('Is Active')
    submit=SubmitField('Add Employee')
    

class TestimonialsForm(FlaskForm):
    name=StringField('Name')
    profession=StringField('Profession')
    info=TextAreaField('Info')
    img=FileField('Img')
    order=IntegerField('Order')
    isActive=BooleanField('Is Active')
    submit=SubmitField('Add Testimonial')