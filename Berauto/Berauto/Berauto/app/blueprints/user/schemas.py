
from marshmallow import Schema, fields

from apiflask.fields import String, Email, Nested, Integer, List

from apiflask.validators import Email

 

class AddressSchema(Schema):

    city= fields.String()

    street= fields.String()

    postalcode = fields.Integer()

 

 

class UserRequestSchema(Schema):

       

    name = fields.String()

    email = String(validate=Email())

    password = fields.String()

    phone = fields.String()

    address = fields.Nested(AddressSchema)
    


    

    class UserResponseSchema(Schema):

        id = fields.Integer()

        name = fields.String()

        email = fields.String()

        address = fields.Nested(AddressSchema)




    

    class UserLoginSchema(Schema):

        email = String(validate=Email())

        password = fields.String()
        



    @bp.post('/registrate')

    @bp.input(UserRequestSchema, location="json")

    @bp.output(UserResponseSchema)

    def user_registrate(json_data):

        success, response = UserService.user_registrate(json_data)

        if success:

            return response, 200

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
