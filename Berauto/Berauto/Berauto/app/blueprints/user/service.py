from app.extensions import db
from app.blueprints.user.schemas import UserResponseSchema
from app.models.user import User
from app.models.address import Address
from app.models.role import Role
from sqlalchemy import select




from datetime import datetime, timedelta

from authlib.jose import jwt

from flask import current_app

@staticmethod

def token_generate(user : User):
    payload = PayloadSchema()
    payload.exp = int((datetime.now()+ timedelta(minutes=30)).timestamp())
    payload.user_id = user.id
    payload.roles = RoleSchema().dump(obj=user.roles, many=True)
    return jwt.encode({'alg': 'RS256'}, PayloadSchema().dump(payload), current_app.config['SECRET_KEY']).decode()





     

class UserService:

       

    @staticmethod
    def user_registrate(request):

        try:

            if db.session.execute(select(User).filter_by(email=request["email"])).scalar_one_or_none():

                return False, "E-mail already exist!"

     

            request["address"] = Address(**request["address"])

            user = User(**request)

            user.set_password(user.password)

            user.roles.append(

                db.session.execute(select(Role).filter_by(name="User")).scalar_one()           

                )

            db.session.add(user)

            db.session.commit()

        except Exception as ex:

            return False, "Incorrect User data!"

        return True, UserResponseSchema().dump(user)

    #@staticmethod
    #def user_login(request):

#        try:
#
#           user = db.session.execute(select(User).filter_by(email=request["email"])).scalar_one()
#
#           if not user.check_password(request["password"]):
#
#            return False, "Incorrect e-mail or password!"
#
#        except Exception as ex:
#
#            return False, "Incorrect Login data!"
#
#        return True, UserResponseSchema().dump(user)



    

@staticmethod

def user_login(request):
    try:

      user = db.session.execute(select(User).filter_by(email=request["email"])).scalar_one()

      if not user.check_password(request["password"]):

          return False, "Incorrect e-mail or password!"

      user_schema = UserResponseSchema().dump(user)

      user_schema["token"] = UserService.token_generate(user)

      return True, user_schema 

    except Exception as ex:

        return False, "Incorrect Login data!"
