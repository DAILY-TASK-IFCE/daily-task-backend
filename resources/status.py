from flask_smorest import Blueprint
from resources.resource import ResourceModel
from schemas.task_fields import TaskFieldsResponseSchema
from models.task_fields import Status
from utils.decorators.is_logged_in import is_logged_in


VALID_TYPE_IDS = {1, 2, 3, 4}

blp = Blueprint("Status", __name__, description="Operations on Statuses")

@blp.route("/status")
class StatusList(ResourceModel): 
    @is_logged_in
    @blp.response(200, TaskFieldsResponseSchema(many=True))
    def get(self):
        status = Status.query.filter(Status.id.in_(VALID_TYPE_IDS)).all()
        return status

@blp.route("/status/<int:id>")
class StatusId(ResourceModel):
    @is_logged_in
    @blp.response(200, TaskFieldsResponseSchema)
    def get(self, id):
        if id not in VALID_TYPE_IDS:
            return {"message": "Tipo inválido."}, 400

        obj = Status.query.get_or_404(id)
        return obj, 200

