from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.user_group import (
    UserGroupQueryParamsSchema,
    UserGroupResponseSchema,
    UserGroupParamsSchema,
)
from models.user_group import UserGroup
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query

blp = Blueprint("UserGroups", __name__, description="Operations on UserGroups")


@blp.route("/user_group")
class UserGroupList(ResourceModel):
    @is_logged_in
    @blp.arguments(UserGroupQueryParamsSchema, location="query")
    @blp.response(200, UserGroupResponseSchema(many=True))
    def get(self, args):
        query = filter_query(UserGroup, args)
        user_groups = query.all()
        return user_groups

    @is_logged_in
    @handle_exceptions
    @blp.arguments(UserGroupParamsSchema)
    @blp.response(201)
    def post(self, new_user_data):
        new_user = UserGroup(**new_user_data)
        self.save_data(new_user)
        return {"message": "Usuário adicionado com sucesso a um grupo"}, 201


@blp.route("/user_group/<int:id>")
class UserGroupId(ResourceModel):
    @is_logged_in
    @blp.response(200, UserGroupResponseSchema)
    def get(self, id):
        user_group = UserGroup.query.get_or_404(id)
        return user_group, 200

    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        user_group = UserGroup.query.get_or_404(id)
        self.delete_data(user_group)
        return {"message": "Usuário com sucesso de um grupo"}, 200
