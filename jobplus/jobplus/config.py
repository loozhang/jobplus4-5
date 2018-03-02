class BaseConfig(object):
    SECRET_KEY='makesure to set very secret key'

class DevelopmentConfig(BaseConfig):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/jobplus4_5?charset=utf8'

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

configs={
        'development':DevelopmentConfig,
        'production':ProductionConfig,
        'testing':TestingConfig
        }
