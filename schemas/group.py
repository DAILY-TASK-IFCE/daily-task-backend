from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID, INVALID_SIZE, REQUIRED_FIELD
from schemas.user_group import UserGroupResponseSchema
from schemas.task_fields import TaskFieldsResponseSchema
class PlainGroupResponseSchema(Schema):
    id = fields.Int()
    team_id = fields.Int()
    name = fields.Str()

class GroupResponseSchema(PlainGroupResponseSchema):
    users = fields.List(fields.Nested(UserGroupResponseSchema))
    tasks = fields.List(fields.Nested(TaskFieldsResponseSchema))

class GroupParamsSchema(Schema):
    team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("team"))) 
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100, error=INVALID_SIZE.format("name")), error_messages=dict(required=REQUIRED_FIELD.format("name")))

class GroupQueryParamsSchema(Schema):
    team_id = fields.Int()
    name = fields.Str()

