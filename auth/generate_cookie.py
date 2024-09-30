from flask import jsonify, make_response
from flask_smorest import Blueprint
from models import User 
from sqlalchemy.exc import IntegrityError
from schemas.cookies import ArgumentGenerateCookieSchema, ResponseGenerateCookieSchema
from resources.resource import ResourceModel
from config import secret_key
import jwt
blp: Blueprint = Blueprint("Generate Cookie", __name__, description="Generate JWT for tests")

def generate_jwt(payload: dict) -> str:
    encoded_jwt: str = jwt.encode(payload, key=str(secret_key))
    return encoded_jwt

@blp.route("/generateCookie")
class GenerateCookie(ResourceModel):
    @blp.arguments(ArgumentGenerateCookieSchema)
    @blp.response(200, ResponseGenerateCookieSchema)
    def post(self, args):
        session_user = {
            "name": args["name"],
            "email": args["email"],
            "photo": args["photo"]
        }
    
        user = User.query.filter_by(email=session_user["email"]).first()
        
        if user is None:
            try:
                user = User(
                    name=session_user["name"],
                    email=session_user["email"],
                    photo=session_user["photo"]
                )
                self.save_data(user)
            except IntegrityError:
                return make_response(jsonify({"error": "Erro ao criar o usuário."}), 500)

        jwt_token = generate_jwt(session_user)
        return make_response(jsonify(
            {
                'Authorization': f'Bearer {jwt_token}'
            }
        ), 200)
