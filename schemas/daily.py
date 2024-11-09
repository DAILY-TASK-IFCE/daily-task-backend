from marshmallow import Schema, fields, validate, ValidationError
from datetime import date
from utils.validations.messages.schemas import INVALID_ID, INVALID_DATE


class DailyResponseSchema(Schema):
    id = fields.Int()
    team_user = fields.Nested("PlainTeamUserResponseSchema")
    date = fields.Date()
    items = fields.List(fields.Nested("ItemResponseSchema"))


def validate_date(value):
    if value < date.today():
        raise ValidationError("A data não pode ser anterior ao dia de hoje.")


class DailyParamsSchema(Schema):
    team_user_id = fields.Int(
        required=True,
        validate=validate.Range(min=1, error=INVALID_ID.format("'User Team'")),
    )


class DailyQueryParamsSchema(Schema):
    team_user_id = fields.Int()
    date = fields.Date()
    filter_by = fields.String()
    order_by = fields.String()
    weeknum = fields.Int()
    monthnum = fields.Int()
    team_id = fields.Int()
