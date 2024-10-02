from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.group import GroupQueryParamsSchema, GroupResponseSchema, GroupParamsSchema
from models.group import Group
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.nest_task import nest_task

blp = Blueprint("Groups", __name__, description="Operations on Groups")

@blp.route("/group")
class UserList(ResourceModel): 
    @is_logged_in
    @blp.arguments(GroupQueryParamsSchema, location="query")
    @blp.response(200, GroupResponseSchema(many=True))
    def get(self, args):
        query = filter_query(Group, args)
        groups = query.all()
        group_dicts = []
        for group in groups:
            group_dict = group.__dict__.copy()
            group_dict["tasks"] = nest_task(group)
            group_dicts.append(group_dict)
        return group_dicts
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(GroupParamsSchema)
    @blp.response(201)
    def post(self, new_group_data):
        if Group.query.filter_by(team_id=new_group_data["team_id"], name=new_group_data["name"]).first():
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
        group_dict = group.__dict__.copy()
        group_dict["tasks"] = nest_task(group)
        return group_dict, 200
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(GroupQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        group = Group.query.get_or_404(id)

        for key, value in args.items():
            if value is not None:
                setattr(group, key, value)

        self.save_data(group)
        return {"message": "Grupo editado com sucesso"}, 200
    
    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        group = Group.query.get_or_404(id)
        self.delete_data(group)
        return {"message": "Grupo deletado com sucesso"}, 200

