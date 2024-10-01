from flask_smorest import Blueprint
from resources.resource import ResourceModel
from schemas.type import TypeResponseSchema, TypeQueryParamsSchema
from models.type import Type
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
import os

TEAM_CREATOR_ID = int(str(os.getenv("TEAM_CREATOR_ID")))
TEAM_ADMIN_ID = int(str(os.getenv("TEAM_ADMIN_ID")))
TEAM_REGULAR_ID = int(str(os.getenv("TEAM_REGULAR_ID")))

VALID_TYPE_IDS = {TEAM_CREATOR_ID, TEAM_ADMIN_ID, TEAM_REGULAR_ID}

blp = Blueprint("Types", __name__, description="Operations on Types")

@blp.route("/type")
class TypeList(ResourceModel): 
    @is_logged_in
    @blp.response(200, TypeResponseSchema(many=True))
    def get(self):
        types = Type.query.filter(Type.id.in_(VALID_TYPE_IDS)).all()
        return types

@blp.route("/type/<int:id>")
class TypeId(ResourceModel):
    @is_logged_in
    @blp.response(200, TypeResponseSchema)
    def get(self, id):
        if id not in VALID_TYPE_IDS:
            return {"message": "Tipo inválido."}, 400

        type_obj = Type.query.get_or_404(id)
        return type_obj, 200

