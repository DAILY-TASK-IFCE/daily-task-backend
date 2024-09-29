from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_NAME, INVALID_DESCRIPTION, INVALID_ID
class TaskResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    status_id = fields.Int()
    priority_id = fields.Int()
    difficulty_id = fields.Int()
    task_type_id = fields.Int()
    users = fields.List(fields.Nested('UserTeamResponseSchema'))
    groups = fields.List(fields.Nested('GroupResponseSchema'))

class TaskFieldsResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    tasks = fields.List(fields.Nested(TaskResponseSchema))

class TaskParamsSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100, error=INVALID_NAME))
    description = fields.Str(required=True, validate=validate.Length(min=1, error=INVALID_DESCRIPTION))
    status_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("'Status'")))
    priority_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("'Priority'")))
    difficulty_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("'Difficulty'")))
    task_type_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("'Task Type'")))

class TaskFieldsParamsSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50, error=INVALID_NAME))

class TaskQueryParamsSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    status_id = fields.Int()
    priority_id = fields.Int()
    difficulty_id = fields.Int()
    task_type_id = fields.Int()

class TaskFieldsQueryParamsSchema(Schema):
    name = fields.Str()
