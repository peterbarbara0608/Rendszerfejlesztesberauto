from app.extensions import db
from app.blueprints.user.schemas import UserResponseSchema, RoleSchema, PayloadSchema
from app.models.user import User
from app.models.address import Address
from app.models.role import Role
from sqlalchemy import select
from datetime import datetime, timedelta
from authlib.jose import jwt
from flask import current_app
from apiflask.exceptions import HTTPError

class UserService:

    @staticmethod
    def token_generate(user: User):
        payload = PayloadSchema()
        payload.exp = int((datetime.now() + timedelta(minutes=30)).timestamp())
        payload.user_id = user.id
        payload.roles = RoleSchema().dump(obj=user.roles, many=True)

        with open('private_key.pem', 'rb') as f:
            private_key = f.read()

        return jwt.encode(
            {'alg': 'RS256'},
            PayloadSchema().dump(payload),
            private_key
        ).decode()

    @staticmethod
    def user_registrate(request):
        existing_user = db.session.execute(
            select(User).filter_by(email=request["email"])
        ).scalar_one_or_none()
        if existing_user:
            raise HTTPError(message="E-mail already exists!", status_code=400)

        try:
            password = request.pop("password", None)
            if not password:
                raise HTTPError(message="Password is required", status_code=400)

            address_data = request.pop("address", None)
            address = Address(**address_data) if address_data else None

            user = User(**request)
            if address:
                user.address = address

            user.set_password(password)

            role_user = db.session.execute(select(Role).filter_by(name="User")).scalar_one()
            user.roles.append(role_user)

            db.session.add(user)
            db.session.commit()

            print("Dumping user to schema...")
            user_data = UserResponseSchema().dump(user)
            print("Dumped user:", user_data)
            return {"success": True, "user": user_data}, 201

        except Exception as ex:
            print("Exception in user_registrate:", ex)
            raise HTTPError(message="Incorrect user data!", status_code=400)

    @staticmethod
    def user_login(request):
        try:
            user = db.session.execute(
                select(User).filter_by(email=request["email"])
            ).scalar_one()

            if not user.check_password(request["password"]):
                raise HTTPError(message="Incorrect e-mail or password!", status_code=401)

            user_schema = UserResponseSchema().dump(user)
            user_schema["token"] = UserService.token_generate(user)

            return {"success": True, "user": user_schema}, 200

        except Exception as ex:
            print("Exception in user_login:", ex)
            raise HTTPError(message="Incorrect login data!", status_code=400)
