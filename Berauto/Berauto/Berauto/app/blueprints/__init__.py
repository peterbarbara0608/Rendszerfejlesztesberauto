from apiflask import APIBlueprint




from app.extensions import auth
from flask import current_app
from authlib.jose import jwt
from datetime import datetime
from apiflask import HTTPError

@auth.verify_token

def verify_token(token):

    try:

       data = jwt.decode(token.encode('ascii'),current_app.config['SECRET_KEY'],)
       if data["exp"] < int(datetime.now().timestamp()):

                return None

       return data

    except:

            return None






bp = APIBlueprint('main', __name__, tag="main")


from app.blueprints.user import bp as bp_user
bp.register_blueprint(bp_user, url_prefix="/user")

from app.blueprints.car import bp as bp_car
bp.register_blueprint(bp_car, url_prefix="/car")

from app.blueprints.administrator import bp as bp_admin
bp.register_blueprint(bp_admin, url_prefix="/admin")

from app.blueprints.rental import bp as bp_rental
bp.register_blueprint(bp_rental, url_prefix="/rental")



from app.models import *

