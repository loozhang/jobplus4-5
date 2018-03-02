from flask import render_template
from jobplus.decorators import admin_required,hr_required, vister_required
from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash
admin = Blueprint('admin', __name__, url_prefix='/admin')
@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')
