class Config:
    SECRET_KEY = '#GgNP$4Ckz@g'
    FLASK_APP = 'app:wsgi.py'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Prod(Config):
    MYSQL_DATABASE_HOST = '108.167.188.38'
    # MYSQL_DATABASE_PORT = '0000'
    MYSQL_DATABASE_USER = 'pertca52_admin'
    MYSQL_DATABASE_PASSWORD = "&B]!(eK+?rvZ"
    MYSQL_DATABASE_DB = "pertca52_data"


class Dev(Config):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////test.db'
