# app/__init__.py
from flask import Flask
from .config import Config
from .extensions import db
from .app.graph import NodeModel

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from .app.routes.users import users_bp
    app.register_blueprint(users_bp)

    return app
