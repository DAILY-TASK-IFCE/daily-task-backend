from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError
from resources.resource import ResourceModel
from schemas.user import UserQueryParamsSchema, UserResponseSchema, UserParamsSchema, UserPatchParamsSchema
from models.user import User
blp = Blueprint("Users", __name__, description="Operations on Users")

@blp.route("/user")
class UserList(ResourceModel):
    @blp.arguments(UserQueryParamsSchema, location="query")
    @blp.response(200, UserResponseSchema(many=True))
    def get(self, args):
        query = User.query
        if args.get("name"):
            query = query.filter(User.name == args["name"])
        if args.get("email"):
            query = query.filter(User.email == args["email"])
        if args.get("photo"):
            query = query.filter(User.photo == args["photo"])
        users = query.all()

        return users

    @blp.arguments(UserParamsSchema)
    @blp.response(201)
    def post(self, new_user_data):
        if User.query.filter_by(email=new_user_data["email"]).first():
            return {"message": "Já existe um usuário com esse email."}, 409

        new_user = User(**new_user_data)
        try:
            self.save_data(new_user)
        except SQLAlchemyError as error:
            return {"message": f"Erro com a ação de inserir um Usuário. Código: {error}"}, 500

        return {"message": "Usuário criado com sucesso"}, 201
    @blp.arguments(UserPatchParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args):
        user = User.query.filter_by(id=args["id"]).first()
        if user is None:
            return {"message":"Usuário não encontrado"}, 400
        
        for key, value in args.items():
            if value is not None:
                setattr(user, key, value)
        try:
            self.save_data(user)
        except SQLAlchemyError as error:
            return {"message": f"Erro com a ação de atualizar um Usuário. Código: {error}"}, 500
        
        return {"message": "Usuário editado com sucesso"}, 200
 
@blp.route("/user/<int:id>")
class UserId(ResourceModel):
    @blp.response(200, UserResponseSchema)
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user is None:
            return {"message": "Usuário não encontrado"}, 400
        return user, 200
    
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if user is None:
            return {"message": "Usuário não encontrado"}, 400
        try:
            self.delete_data(user)
        except SQLAlchemyError as error:
            return {"message": f"Error com a ação de deletar um usuário. Código: {error}"}, 500
        
        return {"message": "Usuário deletado com sucesso"}, 200

