from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID, INVALID_DATE
class DailyLimitTimeResponseSchema(Schema):
    id = fields.Int()
    time_limit = fields.Time()
    team_id = fields.Int()

class DailyLimitTimeQueryParamsSchema(Schema):
    time_limit = fields.Time()

class DailyLimitTimeParamsSchema(Schema):
    time_limit = fields.Time(required=True, error_messages={"required": "É preciso definir o tempo limite."})
    team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("Team")))
