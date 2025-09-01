from app.extensions import db

from app.blueprints.user.schemas import UserResponseSchema

from app.models.user import User

from app.models.address import Address

from app.models.role import Role

 

from sqlalchemy import select