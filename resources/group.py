from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.group import GroupQueryParamsSchema, GroupResponseSchema, GroupParamsSchema
from models.group import Group
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.update_if_present import update_if_present
from utils.functions.add_nested_params import (
    add_nested_params,
    add_nested_params_to_list,
)

blp = Blueprint("Groups", __name__, description="Operations on Groups")


@blp.route("/group")
class UserList(ResourceModel):
    @is_logged_in
    @blp.arguments(GroupQueryParamsSchema, location="query")
    @blp.response(200, GroupResponseSchema(many=True))
    def get(self, args):
        query = filter_query(Group, args)
        groups = query.all()
        return add_nested_params_to_list(groups, ["tasks"])

    @is_logged_in
    @handle_exceptions
    @blp.arguments(GroupParamsSchema)
    @blp.response(201)
    def post(self, new_group_data):
        if Group.query.filter_by(
            team_id=new_group_data["team_id"], name=new_group_data["name"]
        ).first():
            return {"message": "Já existe um grupo nesse time com esse nome."}, 409

        new_group = Group(**new_group_data)
        self.save_data(new_group)
        return {"message": "Grupo criado com sucesso"}, 201


@blp.route("/group/<int:id>")
class UserId(ResourceModel):
    @is_logged_in
    @blp.response(200, GroupResponseSchema)
    def get(self, id):
        group = Group.query.get_or_404(id)
        group_dict = add_nested_params(group, ["tasks"])
        return group_dict, 200

    @is_logged_in
    @handle_exceptions
    @blp.arguments(GroupQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        group = Group.query.get_or_404(id)
        update_if_present(group, args)
        self.save_data(group)
        return {"message": "Grupo editado com sucesso"}, 200

    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        group = Group.query.get_or_404(id)
        self.delete_data(group)
        return {"message": "Grupo deletado com sucesso"}, 200
