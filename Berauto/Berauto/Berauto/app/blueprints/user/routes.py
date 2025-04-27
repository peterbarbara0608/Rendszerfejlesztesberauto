from app.blueprints.user import bp
from app.blueprints.user.schemas import UserRequestSchema, UserResponseSchema, UserLoginSchema
from app.blueprints.user.service import UserService
from apiflask import HTTPError
from app.extensions import auth

@bp.route('/')
def index():
    return 'This is The User Blueprint'


@bp.post('/registrate')
@bp.input(UserRequestSchema, location="json")
@bp.output(UserResponseSchema)
def user_registrate(json_data):
    success, response = UserService.user_registrate(json_data)
    if success:
        return response, 
    raise HTTPError(message=response, status_code=400)
 

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