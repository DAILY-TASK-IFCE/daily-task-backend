from marshmallow import Schema, fields, validate, ValidationError
from datetime import date
from utils.validations.messages.schemas import INVALID_ID, INVALID_DATE
class DailyResponseSchema(Schema):
    id = fields.Int()
    user_team_id = fields.Nested('PlainUserTeamResponseSchema')
    date = fields.Date()
    items = fields.List(fields.Nested('ItemResponseSchema'))

def validate_date(value):
    if value < date.today():
        raise ValidationError("A data não pode ser anterior ao dia de hoje.")

class DailyParamsSchema(Schema):
    user_team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("'User Team'")))
    date = fields.Date(
        required=True, 
        error_messages={"required": INVALID_DATE},
        validate=validate_date
    )

class DailyQueryParamsSchema(Schema):
    user_team_id = fields.Int()
    date = fields.Date()

