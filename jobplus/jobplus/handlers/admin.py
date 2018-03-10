from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash
from jobplus.decorators import admin_required
from jobplus.models import User,db
from jobplus.forms import RegisterForm
from flask_login import current_user
admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
@admin_required
def index():
    return render_template('admin/admin_base.html')


@admin.route('/users')
@admin_required
def user():
    page = request.args.get('page', default=1, type=int)
    pagination = User.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/user_list.html', pagination=pagination)

@admin.route('/users/create',methods=['GET','POST'])
@admin_required
def create_user():
    form =  RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('创建用户成功', 'success')
        return redirect(url_for('admin.user'))
    return render_template('admin/create_user.html', form=form)

@admin.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form =RegisterForm(obj=user)
    if form.validate_on_submit():
        form.update_user(user)
        flash('用户更新成功', 'success')
        return redirect(url_for('admin.user'))
    return render_template('admin/edit_user.html', form=form, user=user)


@admin.route('/users/<int:user_id>/delete',methods=['GET','POST'])
@admin_required
def delete_user(user_id):
    if current_user.id == user_id:
        flash('不能删除自己','success')
        return redirect(url_for('admin.user'))
    user = Course.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('不能删除自己','success')
    return redirect(url_for('admin.user'))

