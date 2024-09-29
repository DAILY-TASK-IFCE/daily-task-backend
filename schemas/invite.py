from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_EMAIL, INVALID_ID, INVALID_SIZE, REQUIRED_FIELD


class InviteResponseSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    team_id = fields.Int()


class InviteParamsSchema(Schema):
    user_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("user")))
    team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("team")))

class InviteQueryParamsSchema(Schema):
    user_id = fields.Int()
    team_id = fields.Int()


