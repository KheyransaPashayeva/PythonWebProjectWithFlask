from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,DateField,PasswordField,SubmitField,TextAreaField,IntegerField,BooleanField,FileField

class LoginForm(FlaskForm):
    user_email=EmailField('Email')
    password=PasswordField('password')
    submit=SubmitField('Login')
    
    
class RegisterForm(FlaskForm):
    user_name=StringField('Name')
    user_email=EmailField('Email')
    password=PasswordField('Password')
    user_info=TextAreaField('Info')
    submit=SubmitField('Register')