from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_SIZE, REQUIRED_FIELD, INVALID_ID

class TeamResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    users = fields.List(fields.Nested('UserTeamResponseSchema'))
    invites = fields.List(fields.Nested('InviteResponseSchema'))
    form_items = fields.List(fields.Nested('FormItemResponseSchema'))
class FormItemResponseSchema(Schema):
    id = fields.Int()
    team_id = fields.Int()
    name = fields.Str()
    user_form_items = fields.List(fields.Nested('UserFormItemResponseSchema'))
class UserFormItemResponseSchema(Schema):
    id = fields.Int()
    user_team_id = fields.Int()
    form_team_id = fields.Int()
class TeamParamsSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100, error=INVALID_SIZE.format("name")), error_messages=dict(required=REQUIRED_FIELD.format("name")))
class FormItemParamsSchema(Schema): 
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100, error=INVALID_SIZE.format("name")), error_messages=dict(required=REQUIRED_FIELD.format("name")))
    team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("team")))
class UserFormItemParamsSchema(Schema):
    user_team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("user_team")))
    form_team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("form_team")))
class TeamQueryParamsSchema(Schema):
    name = fields.Str()
class FormItemQueryParamsSchema(Schema):
    name = fields.Str()
    team_id = fields.Int()
class UserFormItemQueryParamsSchema(Schema):
    user_team_id = fields.Int()
    form_team_id = fields.Int()
