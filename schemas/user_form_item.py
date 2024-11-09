from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID

class UserFormItemResponseSchema(Schema):
    id = fields.Int()
    team_user_id = fields.Int()
    form_item_id = fields.Int()
    content = fields.Str()

class UserFormItemParamsSchema(Schema):
    team_user_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("team_user")))
    form_item_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("form_item")))
    content = fields.Str(required=True, validate=validate.Length(min=1, error="Campo content inválido"))

class UserFormItemQueryParamsSchema(Schema):
    team_user_id = fields.Int()
    form_item_id = fields.Int()
    content = fields.Str()
