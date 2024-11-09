from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.team_user import TeamUserQueryParamsSchema, TeamUserResponseSchema
from models.team_user import TeamUser
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.add_nested_params import add_nested_params, add_nested_params_to_list
from utils.functions.update_if_present import update_if_present
blp = Blueprint("User Teams", __name__, description="Operations on User Teams")

@blp.route("/team_user")
class UserList(ResourceModel): 
    @is_logged_in
    @blp.arguments(TeamUserQueryParamsSchema, location="query")
    @blp.response(200, TeamUserResponseSchema(many=True))
    def get(self, args):
        query = filter_query(TeamUser, args)
        team_users = query.all()
        return add_nested_params_to_list(team_users, ["groups", "tasks", "user_form_items"])

    ## Não tem post de TeamUser, um TeamUser só pode ser criado por Team ou por Invite.    
@blp.route("/team_user/<int:id>")
class UserId(ResourceModel):
    @is_logged_in
    @blp.response(200, TeamUserResponseSchema)
    def get(self, id):
        team_user = TeamUser.query.get_or_404(id)
        team_user_dict = add_nested_params(team_user, ["groups", "tasks", "user_form_items"])
        return team_user_dict, 200
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(TeamUserQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        team_user = TeamUser.query.get_or_404(id)
        update_if_present(team_user, args)
        self.save_data(team_user)
        return {"message": "Usuário do Time editado com sucesso"}, 200
    
    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        team_user = TeamUser.query.get_or_404(id)
        self.delete_data(team_user)
        return {"message": "Usuário deletado com sucesso do time"}, 200

