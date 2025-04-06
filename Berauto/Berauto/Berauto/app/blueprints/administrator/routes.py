from Berauto.Berauto.app.blueprints.administrator.schemas import AdminStratLoginSchema, AdminStratRequestSchema, AdminStratResponseSchema


@bp.route('/')

def index():

    return 'This is The Administrator Blueprint'


@bp.post('/registrate')

@bp.input(AdminStratRequestSchema, location="json")

@bp.output(AdminStratResponseSchema)

def user_registrate(json_data):

    success, response = UserService.user_registrate(json_data)

    if success:

        return response, 200

    raise HTTPError(message=response, status_code=400)

@bp.post('/login')

@bp.doc(tags=["user"])

@bp.input(AdminStratLoginSchema, location="json")

@bp.output(AdminStratResponseSchema)

def user_login(json_data):

    success, response = UserService.user_login(json_data)

    if success:

        return response, 200

    raise HTTPError(message=response, status_code=400)

@bp.post('/login')

@bp.doc(tags=["user"])

@bp.input(AdminStratLoginSchema, location="json")

@bp.output(AdminStratResponseSchema)

def user_login(json_data):

    success, response = UserService.user_login(json_data)

    if success:

        return response, 200

    raise HTTPError(message=response, status_code=400)