""" company list,company detail """
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.models import  User,Job,Company
from jobplus.forms import LoginForm,RegisterForm,CompanyRegisterForm
from flask_login import login_user, logout_user, login_required

company = Blueprint('company',__name__,url_prefix='/company')

@company.route('/<int:company_id>')
def index():
    company = Company.query.order_by(Job.created_at)
    return render_template('company/detail.html',company=company)
