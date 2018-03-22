#coding:utf-8
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
db=SQLAlchemy()
class Base(db.Model):

    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)


user_job = db.Table(
    'user_job',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE')),
    db.Column('job_id', db.Integer, db.ForeignKey('job.id', ondelete='CASCADE'))
)


class User(Base, UserMixin):
    __tablename__ = 'user'

    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    real_name = db.Column(db.String(20))
    phone = db.Column(db.String(11))
    work_years = db.Column(db.SmallInteger)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    resume = db.relationship('Resume', uselist=False)
    collect_jobs = db.relationship('Job', secondary=user_job)
    resume_url = db.Column(db.String(64))

    detail = db.relationship('CompanyDetail', uselist=False)

    is_disable = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User:{}>'.format(self.name)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY

    @property
    def is_staff(self):
        return self.role == self.ROLE_USER

 
class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer,primary_key=True)
    logo_url = db.Column(db.String(256))
    name = db.Column(db.String(32))
    website = db.Column(db.String(32))
    description = db.Column(db.String(128))
    location = db.Column(db.String(32))

class Job(Base):
        __tablename__ = 'job'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(24))
        salary = db.Column(db.Integer, nullable=False)
        location = db.Column(db.String(24))
        tags = db.Column(db.String(128),nullable=True)
        experience = db.Column(db.String(32))
        degree = db.Column(db.String(32))
        description = db.Column(db.String(128))
        is_fulltime = db.Column(db.Boolean, default=True)
        is_open = db.Column(db.Boolean, default=True)
        company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete='CASCADE'))
        job_url = db.Column(db.String(256),nullable=True)
        company = db.relationship('Company', uselist=False)
        def __repr__(self):
             return '<Job {}>'.format(self.name)

class Resume(Base):
    __tablename__ = "resume"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    name = db.Column(db.String(24))
    gender = db.Column(db.String(24))
    phone = db.Column(db.Integer)
    degree = db.Column(db.String(24))
    work_year = db.Column(db.Integer)
    exprience = db.Column(db.String(254))

