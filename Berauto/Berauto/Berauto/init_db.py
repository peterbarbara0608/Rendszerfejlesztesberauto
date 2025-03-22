from __future__ import annotations

from app import db
from app import create_app
from config import Config

app=create_app(config_class=Config)
app.app_context().push()




from app.models.role import Role
from app.models.address import Address
from app.models.user import User
from app.models.rental import Rental
from app.models.car import Car



