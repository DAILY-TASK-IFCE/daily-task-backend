from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID, INVALID_SIZE, REQUIRED_FIELD

class UserGroupResponseSchema(Schema):
    id = fields.Int()
    user = fields.Nested('UserTeamResponseSchema')
    group_id = fields.Int()

class UserGroupParamsSchema(Schema):
    user_team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("user_team")))
    group_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("group")))

class UserGroupQueryParamsSchema(Schema):
    user_team_id = fields.Int()
    group_id = fields.Int()
