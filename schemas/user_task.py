from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID, INVALID_SIZE, REQUIRED_FIELD

class UserTaskResponseSchema(Schema):
    id = fields.Int()
    user_team_id = fields.Int()
    task_id = fields.Int()

class UserTaskParamsSchema(Schema):
    user_team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("user_team")))
    task_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("task")))

class UserTaskQueryParamsSchema(Schema):
    user_team_id = fields.Int()
    task_id = fields.Int()
