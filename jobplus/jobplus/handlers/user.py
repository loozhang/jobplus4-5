""""普通用户和企业用户登录路由"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.models import  User
from jobplus.forms import ResumeForm
from flask_login import login_user, logout_user, login_required,current_user

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UserProfileForm(obj=current_user)
    if form.validate_on_submit():
        form.updated_profile(current_user)
        flash('Profile updated successfully', 'success')
        return redirect(url_for('front.index'))
    return render_template('user/profile.html', form=form)