#from turtle import title

from apiflask import APIFlask
from flask import Flask
from config import Config
from app.extensions import db

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from app.models.role import Role
from sqlalchemy import select


def create_app(config_class=Config):
    app = APIFlask(__name__, json_errors=True, title="Berauto", docs_path="/swagger")
    
    app.config.from_object(config_class)

    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)

    from app.models import user, role, car, address, rental

    from app.blueprints import bp as main_bp
    app.register_blueprint(main_bp, url_prefix="/api")

    return app