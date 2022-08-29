from flask import Flask,redirect,url_for,render_template,request
from app import app_bp

@app_bp.route('/')
def app_index():
    return render_template('app/index.html')

@app_bp.route('/contact')
def app_contact():
    return render_template('app/contact.html')