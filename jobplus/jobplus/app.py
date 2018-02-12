from flask import Flask


def register_extensions(app):
    pass


def register_blueprints(app):

    pass

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    
    register_extensions(app) 
    register_blueprints(app)
     
    return app

