from app.blueprints.user import bp
from app.blueprints.user.schemas import UserRequestSchema, UserResponseSchema, UserLoginSchema
from app.blueprints.user.service import UserService
from apiflask import HTTPError
from app.extensions import auth
from flask import jsonify

import traceback

@bp.route('/')
def index():
    return 'This is The User Blueprint'


@bp.post('/registrate')
@bp.input(UserRequestSchema, location="json")
@bp.output(UserResponseSchema)
def user_registrate(json_data):
    try:
        print("Received data:", json_data)
        success, response = UserService.user_registrate(json_data)
        print("Service response:", success, response)
        if success:
            return response, 200
        raise HTTPError(message=response, status_code=400)
    except Exception as ex:
        traceback.print_exc()
        raise HTTPError(message=f"Incorrect User data: {ex}", status_code=400)


 

@bp.post('/login')
@bp.doc(tags=["user"])
@bp.input(UserLoginSchema, location="json")
@bp.output(UserResponseSchema)
def user_login(json_data):
    success, response = UserService.user_login(json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

#@bp.auth_required(auth)