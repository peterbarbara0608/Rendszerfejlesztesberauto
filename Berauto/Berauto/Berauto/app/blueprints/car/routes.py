from apiflask import APIBlueprint
from apiflask import HTTPError
from app.blueprints.car.schemas import CarRequestSchema, CarResponseSchema, RentalRequestSchema, RentalResponseSchema
from app.blueprints.car.service import CarService

bp = APIBlueprint('car', __name__, tag="Car")

@bp.route('/')
def index():
    return 'This is the Car Blueprint'

@bp.get('/list/')
@bp.output(CarResponseSchema(many=True))
def list_all_cars():
    success, response = CarService.list_all_cars()
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.post('/add')
@bp.input(CarRequestSchema, location="json")
@bp.output(CarResponseSchema)
def add_car(json_data):
    success, response = CarService.add_car(json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.post('/rent')
@bp.input(RentalRequestSchema, location="json")
@bp.output(RentalResponseSchema)
def rent_car(json_data):
    success, response = CarService.rent_car(json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.delete('/return/<int:rental_id>')
def return_car(rental_id):
    success, response = CarService.return_car(rental_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)
