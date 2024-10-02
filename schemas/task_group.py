from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID, INVALID_SIZE, REQUIRED_FIELD

class TaskGroupResponseSchema(Schema):
    id = fields.Int()
    task_id = fields.Int()
    group_id = fields.Int()

class TaskGroupParamsSchema(Schema):
    task_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("task")))
    group_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("group")))

class TaskGroupQueryParamsSchema(Schema):
    task_id = fields.Int()
    group_id = fields.Int()
