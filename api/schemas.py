from marshmallow import fields
from api.extensions import ma


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String()
    email = fields.Email()
    password = fields.String(load_only=True)
