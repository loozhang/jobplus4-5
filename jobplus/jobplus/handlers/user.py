""""普通用户和企业用户登录路由"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.models import  User
from jobplus.forms import ResumeForm
from flask_login import login_user, logout_user, login_required,current_user
from jobplus.decorators import vister_required,hr_required

user = Blueprint('user', __name__, url_prefix='/user')

#用户登录后的首页路由
@vister_required
@user.route('/vister/<user_id>')
def vister_index(user_id):
    """普通用户帐号信息"""
   # user_id = current_user.id
    user = User.query.filter_by(id=user_id).first()
    return render_template('user/vister_index.html',user=user)

@hr_required
@user.route('/hr/')
def hr_index():
    """企业用户帐号信息"""
    user_id = current_user.id
    user = User.query.filter_by(id=user_id).first()
    return render_template('user/hr_index.html',user=user,user_id=user_id)

@vister_required
@user.route('/vister/<user_id>/create')
def resume(user_id):
    """用户简历信息"""
    user_id = current_user.id
    form =ResumeForm()
    if form.validate_on_submit():
        form.greate_resume(user_id)
        flash('简历创建成功','success')
        return redirect(url_for('user.vister_index'))
    return render_template('user/create_resume.html',form=form)
