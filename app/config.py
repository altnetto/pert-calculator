class Config:
    SECRET_KEY = '#GgNP$4Ckz@g'
    FLASK_APP = 'app:wsgi.py'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SESSION_COOKIE_NAME = 'pert-calculator-cookies'
    PERMANENT_SESSION_LIFETIME = 300

class Prod(Config):
    pass

class Dev(Config):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
