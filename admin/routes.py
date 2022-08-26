from flask import Flask,redirect,url_for,render_template,request
from run import app

@app.route('/login',methods=['GET','POST'])
def login():
    from models import Messages,Users,db
    user=Users.query.filter_by(is_active=False).first()
    if request.method=='POST':
       if  request.form['username']==user.user_name and request.form['password']==user.password:
           user.is_active=True
           db.session.commit()
           return redirect('/messages')
       else:
           return redirect('/login')
    return render_template('admin/login.html')

@app.route('/logout',methods=['GET','POST'])
def logout():
    from models import Messages,Users,db
    user=Users.query.filter_by(is_active=True).first()
    user.is_active=False
    db.session.commit()
    return render_template('admin/login.html')