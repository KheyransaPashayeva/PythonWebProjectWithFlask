from flask import Flask,redirect,url_for,render_template,request
from admin import admin_bp
from admin.forms import MessagesForm,ServiceForm,NavbarLinkForm,TeamForm,TestimonialsForm,TransportForm,FeatureForm,FaqsForm,StatsForm
import os
from werkzeug.utils import secure_filename
import random