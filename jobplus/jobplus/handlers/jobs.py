""" 职位详情，职位列表"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.models import  User,Job
from jobplus.forms import LoginForm,RegisterForm,CompanyRegisterForm
from flask_login import login_user, logout_user, login_required

jobs = Blueprint('job',__name__,url_prefix='/job')

@jobs.route('/')
def job_list():
    page = request.args.get('page',default=1,type=int)
    pagination = Job.query.paginate(
        page=page,
        per_page = current_app.config['INDEX_PER_PAGE'],
         error_out = False
         )
    return render_template('job/index.html',pagination=pagination)
    

@jobs.route('/job/<int:job_id>')
def job_detail(job_id):
    job=Job.query.get_or_404(job_id)
    return render_template('job/job_detail.html',job=job)
