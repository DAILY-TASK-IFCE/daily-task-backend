from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID, INVALID_DATE
from utils.validations.messages.daily import INVALID_ITEM_DESCRIPTION
class ItemResponseSchema(Schema):
    id = fields.Int()
    description = fields.Str()
    task_id = fields.Int(allow_none=True)
    daily_id = fields.Int()

class DailyResponseSchema(Schema):
    id = fields.Int()
    user_team_id = fields.Nested('UserTeamResponseSchema')
    date = fields.Date()
    items = fields.List(fields.Nested('ItemResponseSchema'))  # Aninhando o schema de ItemResponse


class DailyParamsSchema(Schema):
    user_team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("'User Team'")))
    date = fields.Date(required=True, error_messages={"required": INVALID_DATE})

class ItemParamsSchema(Schema):
    description = fields.Str(required=True, validate=validate.Length(min=1, error=INVALID_ITEM_DESCRIPTION))
    task_id = fields.Int(allow_none=True, validate=validate.Range(min=1, error=INVALID_ID.format("'Task'")))
    daily_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("'Daily'")))

class DailyQueryParamsSchema(Schema):
    user_team_id = fields.Int()
    date = fields.Date()

class ItemQueryParamsSchema(Schema):
    description = fields.Str()
    task_id = fields.Int()
    daily_id = fields.Int()
