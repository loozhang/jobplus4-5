from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from jobplus.models import db,User
from jobplus.config import configs
from jobplus.handlers import admin,front, user, jobs,companys

def register_extensions(app):
    db.init_app(app)
    Migrate(app,db)
    login_manager = LoginManager()
    login_manager.init_app(app)
    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)
    login_manager.login_view = 'front.login'

def register_blueprints(app):
    for blueprint in (admin,user, jobs, front,companys):
        app.register_blueprint(blueprint)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    
    register_extensions(app) 
    register_blueprints(app)
     
    return app
