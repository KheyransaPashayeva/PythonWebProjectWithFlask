from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,DateField,PasswordField,SubmitField,TextAreaField,IntegerField,BooleanField,FileField

class MessagesForm(FlaskForm):
    name=StringField('Name')
    email=EmailField('Email')
    subject=StringField('Subject')
    message=TextAreaField('Message')
    message_date=DateField('message_date')
    submit=SubmitField('Send message')