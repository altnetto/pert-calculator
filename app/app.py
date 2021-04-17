from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session


db = SQLAlchemy()
sess = Session()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Dev')

    with app.app_context():

        db.init_app(app)
        sess.init_app(app)

        from app.routes.index import index as index_bp

        app.register_blueprint(index_bp)

        return app
