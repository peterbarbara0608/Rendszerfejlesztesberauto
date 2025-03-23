#from turtle import title
from flask import Flask
from config import Config
from app.extensions import db

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    #app=APIFlask(__name__, json_errors = True, title="Berauto", docs_path="/swagger")
    
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    from flask_migrate import Migrate
    migrate = Migrate(app, db)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app