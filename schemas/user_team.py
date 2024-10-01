from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID
from schemas.task import PlainTaskResponseSchema
from schemas.group import PlainGroupResponseSchema
from schemas.user_form_item import UserFormItemResponseSchema
class PlainUserTeamResponseSchema(Schema):
    id = fields.Int()
    type_id = fields.Int()
    user_id = fields.Int()
    team_id = fields.Int()

class UserTeamResponseSchema(Schema):
    id = fields.Int()
    type_id = fields.Int()
    user = fields.Nested('PlainUserResponseSchema')
    team = fields.Nested('PlainTeamResponseSchema')
    tasks = fields.List(fields.Nested(PlainTaskResponseSchema))
    groups = fields.List(fields.Nested(PlainGroupResponseSchema))
    user_form_items = fields.List(fields.Nested(UserFormItemResponseSchema))


class UserTeamParamsSchema(Schema):
    user_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("user")))
    team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("team")))
    type_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("type")))

class UserTeamQueryParamsSchema(Schema):
    user_id = fields.Int()
    team_id = fields.Int()
    type_id = fields.Int()


