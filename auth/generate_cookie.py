import jwt
from flask_smorest import Blueprint
from flask.views import MethodView
from schemas import ArgumentGenerateCookieSchema, ResponseGenerateCookieSchema
from flask import jsonify, make_response, Response
from config import secret_key

blp: Blueprint = Blueprint("Generate Cookie", __name__, description="Generate JWT for tests")


def generate_jwt(payload: dict) -> str:
    encoded_jwt: str = jwt.encode(payload, key=str(secret_key))
    return encoded_jwt


@blp.route("/generateCookie")
class GenerateCookie(MethodView):
    @blp.arguments(ArgumentGenerateCookieSchema)
    @blp.response(200, ResponseGenerateCookieSchema)
    def post(self, args: dict) -> Response:
        session_user = {
            "name": args["name"],
            "email": args["email"],
            "photo": args["photo"]
        }
        jwt_token = generate_jwt(session_user)
        return make_response(jsonify(
            {
                'Authorization': f'Bearer {jwt_token}'
            }
        ), 200)
