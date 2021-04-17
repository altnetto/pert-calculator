class Config:
    SECRET_KEY = '#GgNP$4Ckz@g'
    FLASK_APP = 'app:wsgi.py'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Prod(Config):
    pass

class Dev(Config):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
