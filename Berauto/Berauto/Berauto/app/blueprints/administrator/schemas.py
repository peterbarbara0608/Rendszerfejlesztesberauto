from app.extensions import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer
from sqlalchemy import ForeignKey

from marshmallow import Schema, fields

from apiflask.fields import String, Email, Nested, Integer, List

from apiflask.validators import Email

 

class AddressSchema(Schema):

    city= fields.String()

    street= fields.String()

    postalcode = fields.Integer()
 

class AdminStratRequestSchema(Schema):

    name = fields.String()

    email = String(validate=Email())

    password = fields.String()

    phone = fields.String()

    address = fields.Nested(AddressSchema)


class AdminStratResponseSchema(Schema):

    id = fields.Integer()

    name = fields.String()

    email = fields.String()

    address = fields.Nested(AddressSchema)

class AdminStratLoginSchema(Schema):

    email = String(validate=Email())

    password = fields.String()

