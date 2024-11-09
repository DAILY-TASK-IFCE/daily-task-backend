from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID
from utils.validations.messages.daily import INVALID_ITEM_DESCRIPTION


class ItemResponseSchema(Schema):
    id = fields.Int()
    description = fields.Str()
    task_id = fields.Int(allow_none=True)
    daily_id = fields.Int()


class ItemParamsSchema(Schema):
    description = fields.Str(
        required=True, validate=validate.Length(min=1, error=INVALID_ITEM_DESCRIPTION)
    )
    task_id = fields.Int(
        allow_none=True,
        validate=validate.Range(min=1, error=INVALID_ID.format("'Task'")),
    )
    daily_id = fields.Int(
        required=True,
        validate=validate.Range(min=1, error=INVALID_ID.format("'Daily'")),
    )


class ItemQueryParamsSchema(Schema):
    description = fields.Str()
    task_id = fields.Int()
    daily_id = fields.Int()
