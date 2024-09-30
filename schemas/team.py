from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_SIZE, REQUIRED_FIELD
from schemas.user_team import PlainUserTeamResponseSchema
from schemas.invite import InviteResponseSchema
from schemas.form_item import PlainFormItemResponseSchema
class PlainTeamResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()

class TeamResponseSchema(PlainTeamResponseSchema):
    users = fields.List(fields.Nested(PlainUserTeamResponseSchema))
    invites = fields.List(fields.Nested(InviteResponseSchema))
    form_items = fields.List(fields.Nested(PlainFormItemResponseSchema))

class TeamParamsSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100, error=INVALID_SIZE.format("name")), error_messages=dict(required=REQUIRED_FIELD.format("name")))

class TeamQueryParamsSchema(Schema):
    name = fields.Str()

