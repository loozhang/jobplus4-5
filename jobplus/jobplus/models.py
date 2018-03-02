#coding:utf-8
from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
db=SQLAlchemy()
class Base(db.Model):

    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
class User(Base,UserMixin):
    __tablename__ = 'user'
    ROLE_VISTER = 10
    ROLE_HR = 20
    ROLE_ADMIN = 30
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=False)
##用户名 可以公司名或者用户名字
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
##注册邮箱，用户用户登录
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_VISTER)
    def __repr__(self):
        return "<User:{}>".format(self.username)
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,orig_password):
        self._password = generate_password_hash(orig_password)
    def check_password(self,password):
        return check_password_hash(self._password,password)
    @property
    def is_HR(self):
        return self.role == self.ROLE_HR
    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

 
class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer,primary_key=True)
    logo_url = db.Column(db.String(256))
    name = db.Column(db.String(32))
    website = db.Column(db.String(32))
    description = db.Column(db.String(128))
    address = db.Column(db.String(32))
    job_numbers = db.Column(db.Integer)

class Job(Base):
        __tablename__ = 'job'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(24))
        salary_low = db.Column(db.Integer, nullable=False)
        salary_high = db.Column(db.Integer, nullable=False)
        location = db.Column(db.String(24))
        tags = db.Column(db.String(128))
        experience_requirement = db.Column(db.String(32))
        degree_requirement = db.Column(db.String(32))
        is_fulltime = db.Column(db.Boolean, default=True)
        is_open = db.Column(db.Boolean, default=True)
        company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete='CASCADE'))
        company = db.relationship('Company', uselist=False)
        def __repr__(self):
             return '<Job {}>'.format(self.name)
