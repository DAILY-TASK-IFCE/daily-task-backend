from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID

class UserFormItemResponseSchema(Schema):
    id = fields.Int()
    user_team_id = fields.Int()
    form_team_id = fields.Int()

class UserFormItemParamsSchema(Schema):
    user_team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("user_team")))
    form_team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("form_team")))

class UserFormItemQueryParamsSchema(Schema):
    user_team_id = fields.Int()
    form_team_id = fields.Int()
