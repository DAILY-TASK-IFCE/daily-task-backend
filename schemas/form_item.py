from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_SIZE, REQUIRED_FIELD, INVALID_ID

class PlainFormItemResponseSchema(Schema):
    id = fields.Int()
    team_id = fields.Int()
    name = fields.Str()

class FormItemResponseSchema(PlainFormItemResponseSchema):
    user_form_items = fields.List(fields.Nested('UserFormItemResponseSchema'))

class FormItemParamsSchema(Schema): 
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100, error=INVALID_SIZE.format("name")), error_messages=dict(required=REQUIRED_FIELD.format("name")))
    team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("team")))

class FormItemQueryParamsSchema(Schema):
    name = fields.Str()
    team_id = fields.Int()


