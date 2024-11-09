from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID, INVALID_SIZE, REQUIRED_FIELD


class UserGroupResponseSchema(Schema):
    id = fields.Int()
    team_user_id = fields.Int()
    group_id = fields.Int()


class UserGroupParamsSchema(Schema):
    team_user_id = fields.Int(
        required=True,
        validate=validate.Range(min=1, error=INVALID_ID.format("team_user")),
    )
    group_id = fields.Int(
        required=True, validate=validate.Range(min=1, error=INVALID_ID.format("group"))
    )


class UserGroupQueryParamsSchema(Schema):
    team_user_id = fields.Int()
    group_id = fields.Int()
