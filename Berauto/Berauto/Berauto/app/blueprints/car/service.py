from app.extensions import db
from app.models.car import Car
from app.models.rental import Rental
from sqlalchemy import select, and_
from app.blueprints.car.schemas import CarResponseSchema, RentalResponseSchema

class CarService:
    @staticmethod
    def add_car(request):
        try:
            car = Car(**request)
            db.session.add(car)
            db.session.commit()
        except Exception:
            return False, "Error adding car."
        return True, CarResponseSchema().dump(car)

    @staticmethod
    def list_all_cars():
        cars = db.session.execute(select(Car)).scalars()
        return True, CarResponseSchema().dump(cars, many=True)

    @staticmethod
    def rent_car(request):
        try:
            rental = Rental(**request)
            db.session.add(rental)
            db.session.commit()
        except Exception:
            return False, "Error renting car."
        return True, RentalResponseSchema().dump(rental)

    @staticmethod
    def return_car(rental_id):
        try:
            rental = db.session.get(Rental, rental_id)
            if rental:
                db.session.delete(rental)
                db.session.commit()
        except Exception:
            return False, "Error returning car."
        return True, "Car returned successfully."