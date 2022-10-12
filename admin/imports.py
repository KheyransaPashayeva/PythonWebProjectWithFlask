from flask import Flask,redirect,url_for,render_template,request
from admin import admin_bp
from admin.forms import ServiceForm,NavbarLinkForm,TeamForm,TestimonialsForm,TransportForm,FeatureForm,FaqsForm,StatsForm,SocialMediaForm,TeamSocialForm,PricingForm
import os
from werkzeug.utils import secure_filename
import random
from flask_login import login_required,current_user