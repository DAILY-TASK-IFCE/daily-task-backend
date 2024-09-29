from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_EMAIL, INVALID_ID, INVALID_SIZE, REQUIRED_FIELD

class UserResponseSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    photo = fields.Str()
    name = fields.Str()
    teams = fields.List(fields.Nested('TeamResponseSchema'))

class UserTeamResponseSchema(Schema):
    id = fields.Int()
    user = fields.Nested('UserResponseSchema')
    team = fields.Nested('TeamResponseSchema')
    type_id = fields.Int()
    tasks = fields.List(fields.Nested('TaskResponseSchema'))
    groups = fields.List(fields.Nested('GroupResponseSchema'))
    user_form_items = fields.List(fields.Nested('UserFormItemResponseSchema'))

class TypeResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    user_teams = fields.List(fields.Nested('UserTeamResponseSchema'))

class InviteResponseSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    team_id = fields.Int()

class UserParamsSchema(Schema):
    email = fields.Str(required=True, validate=validate.And(
    validate.Length(min=1, max=120,
                    error=INVALID_EMAIL),
    validate.Regexp(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,}(\.\w{2,})?(\.\w{2,})?$",
                    error=INVALID_EMAIL)),
                    error_messages=dict(required=REQUIRED_FIELD.format("email")))
    photo = fields.Str(required=False, validate=validate.Length(min=1, max=255, error=INVALID_SIZE.format("photo")))
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100, error=INVALID_SIZE.format("name")), error_messages=dict(required=REQUIRED_FIELD.format("name")))

class UserTeamParamsSchema(Schema):
    user_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("user")))
    team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("team")))
    type_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("type")))

class TypeParamsSchema(Schema): 
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100, error=INVALID_SIZE.format("name")), error_messages=dict(required=REQUIRED_FIELD.format("name")))

class InviteParamsSchema(Schema):
    user_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("user")))
    team_id = fields.Int(required=True, validate=validate.Range(min=1, error=INVALID_ID.format("team")))
class UserQueryParamsSchema(Schema):
    email = fields.Str()
    photo = fields.Str()
    name = fields.Str()

class UserTeamQueryParamsSchema(Schema):
    user_id = fields.Int()
    team_id = fields.Int()
    type_id = fields.Int()

class TypeQueryParamsSchema(Schema):
    name = fields.Str()

class InviteQueryParamsSchema(Schema):
    user_id = fields.Int()
    team_id = fields.Int()
