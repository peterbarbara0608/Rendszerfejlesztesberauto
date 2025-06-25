from Berauto.Berauto.app.blueprints.ugyintezo.schemas import UgyintezoLoginSchema, UgyintezoRequestSchema, UgyintezoResponseSchema, UgyintezoStratLoginSchema


@bp.route('/')

def index():

    return 'This is The Clerk Blueprint'

@bp.post('/registrate')

@bp.input(UgyintezoRequestSchema, location="json")

@bp.output(UgyintezoResponseSchema)

def user_registrate(json_data):

    success, response = UserService.user_registrate(json_data)

    if success:

        return response, 200

    raise HTTPError(message=response, status_code=400)

@bp.post('/login')

@bp.doc(tags=["user"])

@bp.input(UgyintezoLoginSchema, location="json")

@bp.output(UgyintezoResponseSchema)

def user_login(json_data):

    success, response = UserService.user_login(json_data)

    if success:

        return response, 200

    raise HTTPError(message=response, status_code=400)

@bp.post('/login')

@bp.doc(tags=["user"])

@bp.input(UgyintezoLoginSchema, location="json")

@bp.output(UgyintezoResponseSchema)

def user_login(json_data):

    success, response = UserService.user_login(json_data)

    if success:

        return response, 200

    raise HTTPError(message=response, status_code=400)