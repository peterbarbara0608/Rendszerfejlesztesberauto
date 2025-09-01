from marshmallow import Schema, fields
from apiflask.fields import Integer, String, DateTime, Nested
from app.models.car import Car
from app.models.user import User

class CarRequestSchema(Schema):
    brand = fields.String()
    model = fields.String()
    year = fields.Integer()

class CarResponseSchema(Schema):
    id = fields.Integer()
    brand = fields.String()
    model = fields.String()
    year = fields.Integer()

class RentalRequestSchema(Schema):
    user_id = fields.Integer()
    car_id = fields.Integer()
    start_date = fields.DateTime()
    end_date = fields.DateTime()

class RentalResponseSchema(Schema):
    id = fields.Integer()
    user = fields.Nested("UserResponseSchema")
    car = fields.Nested(CarResponseSchema)
    start_date = fields.DateTime()
    end_date = fields.DateTime()