from marshmallow import Schema, fields

class ArgumentGenerateCookieSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    photo = fields.Str(required=True)

class ResponseGenerateCookieSchema(Schema):
    authorization = fields.Str()
