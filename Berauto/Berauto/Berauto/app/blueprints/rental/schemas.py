from marshmallow import Schema, fields

class RentalCreateSchema(Schema):
    car_model = fields.String(required=True)
    renter_name = fields.String(required=True)
    rental_date = fields.Date(required=True)
    return_date = fields.Date(required=False)
    price = fields.Float(required=False)

class RentalResponseSchema(Schema):
    rental_id = fields.Integer()
    car_model = fields.String()
    renter_name = fields.String()
    rental_date = fields.String()
    return_date = fields.String()
    price = fields.Float()
