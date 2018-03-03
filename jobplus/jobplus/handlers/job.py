""" 职位详情，职位列表"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.models import  User,Job
from jobplus.forms import LoginForm,RegisterForm,CompanyRegisterForm
from flask_login import login_user, logout_user, login_required

job = Blueprint('job',__name__,url_prefix='/job')

@job.route('/')
def index():
    job = Job.query.order_by(Job.created_at).limit(10).all()
    return render_template('job.html',job=job)
