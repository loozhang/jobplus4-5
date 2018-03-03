from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.models import  User
from jobplus.forms import LoginForm,RegisterForm,CompanyRegisterForm
from flask_login import login_user, logout_user, login_required


user = Blueprint('vister', __name__, url_prefix='/vister')

@user.route('/')
def vister_index():
    return render_template('')
