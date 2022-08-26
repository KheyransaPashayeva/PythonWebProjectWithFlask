from flask import Flask,redirect,url_for,render_template,request
from run import app

@app.route('/login',methods=['GET','POST'])
def login():
    
   return render_template('admin/login.html')