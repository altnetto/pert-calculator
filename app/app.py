from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Dev')

    db.init_app(app)

    from app.routes.index import index as index_bp

    app.register_blueprint(index_bp)

    return app