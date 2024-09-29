from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_EMAIL, INVALID_SIZE, REQUIRED_FIELD
from schemas.team import PlainTeamResponseSchema
class PlainUserResponseSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    photo = fields.Str()
    name = fields.Str()

class UserResponseSchema(PlainUserResponseSchema):
    teams = fields.List(fields.Nested(PlainTeamResponseSchema))

class UserParamsSchema(Schema):
    email = fields.Str(required=True, validate=validate.And(
    validate.Length(min=1, max=120,
                    error=INVALID_EMAIL),
    validate.Regexp(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,}(\.\w{2,})?(\.\w{2,})?$",
                    error=INVALID_EMAIL)),
                    error_messages=dict(required=REQUIRED_FIELD.format("email")))
    photo = fields.Str(required=False, validate=validate.Length(min=1, max=255, error=INVALID_SIZE.format("photo")))
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100, error=INVALID_SIZE.format("name")), error_messages=dict(required=REQUIRED_FIELD.format("name")))

class UserQueryParamsSchema(Schema):
    email = fields.Str()
    photo = fields.Str()
    name = fields.Str()

