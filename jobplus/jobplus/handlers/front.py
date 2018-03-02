#coding:utf-8
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.models import  User
from jobplus.forms import LoginForm,RegisterForm,CompanyRegisterForm
from flask_login import login_user, logout_user, login_required

front = Blueprint('front', __name__)


@front.route('/')
def index():
    return render_template('index.html')

@front.route('/vister')
def vister_index():
    return render_template('vister/index.html')

@front.route('/hr')
def hr_index():
    return render_template('hr/index.html')

@front.route('/admin')
def admin_index():
    return render_template('admin/index.html')


@front.route('/job')
def job():
    return render_template('job.html')

@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        if user.role == 10:
            return redirect(url_for('.vister_index'))
#           return render_template('ceshi.html', form=form)
        elif user.role== 20:
            return redirect(url_for('.hr_index'))
        elif user.role== 30:
            return redirect(url_for('.admin_index'))
    return render_template('login.html', form=form)

@front.route('/reigster-vister',methods=['GET','POST'])
def register_vister():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()

        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('register/register_vister.html', form=form)
@front.route('/reigster-hr',methods=['GET','POST'])
def register_hr():
    form = CompanyRegisterForm()
    form.test()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('register/register_hr.html', form=form)


@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出登录', 'success')
    return redirect(url_for('.index'))

