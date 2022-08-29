from flask import Flask,redirect,url_for,render_template,request
from admin import admin_bp

@admin_bp.route('/')
def admin_index():
    return render_template('admin/index.html')