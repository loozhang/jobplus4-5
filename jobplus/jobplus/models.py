from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db=SQLalchemy()
class User(db.Model):
    __tablename__ == 'user'
    id = db.Column(db.Integer,primary_key=True)
    type = db.Column(db.String(32)

class Job(db.Model):
    __tablename__ == 'job'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    salary = db.Column(db.Integer)
    experience = db.Column(db.String(32))
    address = db.Column(db.String(32))
    companyinfo = db.Column(db.String(32)),db.Foreignkey('company.name')
    create_time = db.Column(db.DateTime,default=datetime.utcnow)

class Company(db.Model):
    __tablename__ == 'company'
    id = db.Column(db.Integer,primary_key=True)
    logo_url = db.Column(db.String(256))
    name = db.Column(db.String(32))
    website = db.Column(db.String(32))
    description = db.Column(db.String(128))
    address = db.Column(db.String(32))
    job_numbers = db.Column(db.Integer)

