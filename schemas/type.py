from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_SIZE, REQUIRED_FIELD

class TypeResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    user_teams = fields.List(fields.Nested('PlainUserTeamResponseSchema'))


class TypeParamsSchema(Schema): 
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100, error=INVALID_SIZE.format("name")), error_messages=dict(required=REQUIRED_FIELD.format("name")))


class TypeQueryParamsSchema(Schema):
    name = fields.Str()


