from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,DateField,PasswordField,SubmitField,TextAreaField,IntegerField,BooleanField,FileField

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

class TeamGalleryForm(FlaskForm):
    pass

class TestimonialsForm(FlaskForm):
    name=StringField('Name')
    profession=StringField('Profession')
    info=TextAreaField('Info')
    img=FileField('Img')
    order=IntegerField('Order')
    isActive=BooleanField('Is Active')
    submit=SubmitField('Add Testimonial')
    
    
class TransportForm(FlaskForm):
    transport_title=StringField('TransportTitle')
    transport_text=TextAreaField('TransportText')
    transport_img=StringField('TransportIMG')
    transport_url=StringField('TransportUrl')
    submit=SubmitField('Add transport')
    
class FeatureForm(FlaskForm):
    feature_title=StringField('FeatureTitle')
    feature_img=FileField('FeatureIMG')
    feature_text=TextAreaField('FeatureText')
    feature_orderimg=StringField('Feature orderimg')
    feature_ordertext=StringField('Feature ordertext')
    is_active=BooleanField('Is Active')
    submit=SubmitField('Add feature')
    
    
class FaqsForm(FlaskForm):
    faq_question=StringField('FaqQuestion')
    faq_answer=StringField('FaqQuestion')
    submit=SubmitField('Add faq')
    
class StatsForm(FlaskForm):
    name=StringField('name')
    value=IntegerField('value')
    submit=SubmitField('Add stat')

class SocialMediaForm(FlaskForm):
    social_name=StringField('Social name')
    social_icon=StringField('Social icon')
    social_url=StringField('Social url')
    submit=SubmitField('Add socialmedia')
    
class TeamSocialForm(FlaskForm):
    social_name=StringField('Social name')
    social_icon=StringField('Social icon')
    social_url=StringField('Social url')
    submit=SubmitField('Add socialmedia')