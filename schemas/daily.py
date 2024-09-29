from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID, INVALID_DATE
class DailyResponseSchema(Schema):
    id = fields.Int()
    user_team_id = fields.Nested('PlainUserTeamResponseSchema')
    date = fields.Date()
    items = fields.List(fields.Nested('ItemResponseSchema'))


class DailyParamsSchema(Schema):
    user_team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("'User Team'")))
    date = fields.Date(required=True, error_messages={"required": INVALID_DATE})

class DailyQueryParamsSchema(Schema):
    user_team_id = fields.Int()
    date = fields.Date()

