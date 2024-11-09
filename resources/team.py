from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.team import TeamQueryParamsSchema, TeamResponseSchema, TeamParamsSchema
from models.team import Team
from models.team_user import TeamUser
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.get_logged_in_user import get_logged_in_user
from utils.functions.update_if_present import update_if_present
import os
from dotenv import load_dotenv
load_dotenv()


blp = Blueprint("Teams", __name__, description="Operations on Teams")

@blp.route("/team")
class TeamList(ResourceModel):
    @is_logged_in
    @blp.arguments(TeamQueryParamsSchema, location="query") 
    @blp.response(200, TeamResponseSchema(many=True))
    def get(self, args):
        query = filter_query(Team, args)
        teams = query.order_by(Team.id.desc()).all()
        return teams
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(TeamParamsSchema)
    @blp.response(201)
    def post(self, new_team_data):
        user = get_logged_in_user()
        new_team = Team(**new_team_data)
        self.save_data(new_team)
        team_user = TeamUser(user_id=user.id, team_id=new_team.id, type_id=os.getenv("TEAM_CREATOR_ID"))
        self.save_data(team_user)
        return {"message": "Time criado com sucesso."}, 201

@blp.route("/team/<int:id>")
class TeamId(ResourceModel):     
    @is_logged_in
    @blp.response(200, TeamResponseSchema)
    def get(self, id):
        team = Team.query.get_or_404(id)
        return team, 200       
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(TeamQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        team = Team.query.get_or_404(id)
        update_if_present(team, args)
        self.save_data(team)
        return {"message": "Time editado com sucesso"}, 200
    
    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        team = Team.query.get_or_404(id)
        self.delete_data(team)
        return {"message": "Time deletado com sucesso"}, 200

