from __future__ import annotations

from app import db
from app import create_app
from config import Config

app = create_app(config_class=Config)

app.app_context().push()


