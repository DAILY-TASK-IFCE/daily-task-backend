from flask_smorest import Blueprint

from models.team_user import TeamUser
from resources.resource import ResourceModel
from schemas.invite import InviteQueryParamsSchema, InviteResponseSchema, InviteParamsSchema
from models.invite import Invite
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
import os
from dotenv import load_dotenv

load_dotenv()
blp = Blueprint("Invites", __name__, description="Operations on Invites")

@blp.route("/invite")
class InviteList(ResourceModel): 
    @is_logged_in
    @blp.arguments(InviteQueryParamsSchema, location="query")
    @blp.response(200, InviteResponseSchema(many=True))
    def get(self, args):
        query = filter_query(Invite, args)
        invites = query.order_by(Invite.id.desc()).all()
        return invites
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(InviteParamsSchema)
    @blp.response(201)
    def post(self, new_invite_data):
        if Invite.query.filter_by(user_id=new_invite_data["user_id"], team_id=new_invite_data["team_id"]).first():
            return {"message": "Já existe um convite desse time para esse usuário."}, 409

        new_invite = Invite(**new_invite_data)
        self.save_data(new_invite)
        return {"message": "Convite criado com sucesso"}, 201

@blp.route("/invite/<int:id>")
class InviteId(ResourceModel):
    @is_logged_in
    @blp.response(200, InviteResponseSchema)
    def get(self, id):
        user = Invite.query.get_or_404(id)
        return user, 200
    
@blp.route("/invite/accept/<int:id>")
class AcceptInviteId(ResourceModel): 
    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        invite = Invite.query.get_or_404(id)
        new_team_user = TeamUser(user_id=invite.user_id, team_id=invite.team_id, type_id=os.getenv("TEAM_REGULAR_ID"))
        self.save_data(new_team_user)
        self.delete_data(invite)
        return {"message": "Convite aceito e usuário adicionado ao time."}, 200

@blp.route("/invite/deny/<int:id>")
class DenyInviteId(ResourceModel): 
    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        invite = Invite.query.get_or_404(id)
        self.delete_data(invite)
        return {"message": "Convite negado e deletado."}, 200
