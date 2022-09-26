from flask import Flask,redirect,url_for,render_template,request,flash
from auth import auth_bp
from auth.forms import LoginForm,RegisterForm
import re

@auth_bp.route('/')
def auth_index():
    return render_template('auth/index.html')

@auth_bp.route('/login',methods=['GET','POST'])
def auth_login():
    loginForm=LoginForm()
    from models import Users
    from run import db
    if request.method=='POST':
        for user in Users.query.all():
            if user.user_email==loginForm.user_email.data and user.password==loginForm.password.data:  
                return redirect(url_for('admin.admin_index'))
         
    return render_template('auth/login.html',loginForm=loginForm)


@auth_bp.route('/register',methods=['GET','POST'])
def auth_register():
    from models import Users
    from run import db
    registerForm=RegisterForm()
    if request.method=='POST':
        password=registerForm.password.data
        if(re.search(r'[A-Z][a-z]', password) and len(password) >5 and len(password)< 10):
            
            user=Users( user_name=registerForm.user_name.data,user_email=registerForm.user_email.data,
                        password=password,user_info=registerForm.user_info.data
                      )
            db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.auth_login'))
    return render_template('auth/register.html',registerForm=registerForm)

@auth_bp.route('/logout',methods=['GET','POST'])
def auth_logout():
    return redirect(url_for('auth.auth_login'))
    