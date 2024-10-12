from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.user_team import UserTeamQueryParamsSchema, UserTeamResponseSchema
from models.user_team import UserTeam
from models.user_form_item import UserFormItem
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.nest_group import nest_group
from utils.functions.nest_task import nest_task
blp = Blueprint("User Teams", __name__, description="Operations on User Teams")

@blp.route("/user_team")
class UserList(ResourceModel): 
    @is_logged_in
    @blp.arguments(UserTeamQueryParamsSchema, location="query")
    @blp.response(200, UserTeamResponseSchema(many=True))
    def get(self, args):
        query = filter_query(UserTeam, args)
        user_teams = query.all()
        user_team_dicts = []
        for user_team in user_teams:
            user_team_dict = user_team.__dict__.copy()
            user_team_dict["groups"] = nest_group(user_team)
            user_team_dict["tasks"] = nest_task(user_team)
            user_team_dict["user_form_items"] = UserFormItem.query.filter(user_team_id=user_team.id).all()
            user_team_dicts.append(user_team_dict)
        return user_team_dicts

    ## Não tem post de UserTeam, um UserTeam só pode ser criado por Team ou por Invite.    
@blp.route("/user_team/<int:id>")
class UserId(ResourceModel):
    @is_logged_in
    @blp.response(200, UserTeamResponseSchema)
    def get(self, id):
        user_team = UserTeam.query.get_or_404(id)
        user_team_dict = user_team.__dict__.copy()
        user_team_dict["groups"] = nest_group(user_team)
        user_team_dict["tasks"] = nest_task(user_team)
        user_team_dict["user_form_items"] = UserFormItem.query.filter(user_team_id=user_team.id).all()
        return user_team_dict, 200
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(UserTeamQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        user_team = UserTeam.query.get_or_404(id)

        for key, value in args.items():
            if value is not None:
                setattr(user_team, key, value)

        self.save_data(user_team)
        return {"message": "Usuário do Time editado com sucesso"}, 200
    
    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        user_team = UserTeam.query.get_or_404(id)
        self.delete_data(user_team)
        return {"message": "Usuário deletado com sucesso do time"}, 200

