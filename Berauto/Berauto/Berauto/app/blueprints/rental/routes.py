from app.blueprints.rental import bp
from apiflask import HTTPError
from app.blueprints.rental.service import RentalService
from app.blueprints.rental.schemas import RentalCreateSchema, RentalResponseSchema

@bp.route('/')
@bp.doc(tags=["rental"])
def index():
    return 'This is the Rental Blueprint'

@bp.post('/create')
@bp.doc(tags=["rental"])
@bp.input(RentalCreateSchema, location="json")
@bp.output(RentalResponseSchema)
def create_rental(json_data):
    success, response = RentalService.create_rental(json_data)
    if success:
        return response, 201
    raise HTTPError(message=response, status_code=400)

@bp.get('/<int:rental_id>')
@bp.doc(tags=["rental"])
@bp.output(RentalResponseSchema)
def get_rental(rental_id):
    success, response = RentalService.get_rental(rental_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=404)
