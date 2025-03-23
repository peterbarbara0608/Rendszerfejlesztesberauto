#from turtle import title
from apiflask import APIFlask
from config import Config
from app.extensions import db

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate


def create_app(config_class=Config):
    #app = Flask(__name__)
    app=APIFlask(__name__, json_errors = True, title="Berauto", docs_path="/swagger")
    
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    from flask_migrate import Migrate
    migrate = Migrate(app, db, render_as_batch=True)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix="/api")

    return app