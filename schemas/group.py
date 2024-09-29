from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID, INVALID_SIZE, REQUIRED_FIELD

class GroupResponseSchema(Schema):
    id = fields.Int()
    team_id = fields.Int()
    name = fields.Str()
    users = fields.List(fields.Nested('UserGroupResponseSchema'))
    tasks = fields.List(fields.Nested('TaskGroupResponseSchema'))
class UserGroupResponseSchema(Schema):
    id = fields.Int()
    user = fields.Nested('UserTeamResponseSchema')
    group_id = fields.Int()
class GroupParamsSchema(Schema):
    team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("team"))) 
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100, error=INVALID_SIZE.format("name")), error_messages=dict(required=REQUIRED_FIELD.format("name")))
class UserGroupParamsSchema(Schema):
    user_team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("user_team")))
    group_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("group")))
class GroupQueryParamsSchema(Schema):
    team_id = fields.Int()
    name = fields.Str()
class UserGroupQueryParamsSchema(Schema):
    user_team_id = fields.Int()
    group_id = fields.Int()
