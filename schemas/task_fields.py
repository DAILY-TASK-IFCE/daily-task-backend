from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_NAME

class TaskFieldsResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    tasks = fields.List(fields.Nested('TaskResponseSchema'))


class TaskFieldsParamsSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50, error=INVALID_NAME))


class TaskFieldsQueryParamsSchema(Schema):
    name = fields.Str()
