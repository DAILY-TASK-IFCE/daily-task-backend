from flask_smorest import Blueprint
from resources.resource import ResourceModel
from schemas.task_fields import TaskFieldsResponseSchema
from models.task_fields import Priority
from utils.decorators.is_logged_in import is_logged_in


VALID_TYPE_IDS = {1, 2, 3, 4}

blp = Blueprint("Priority", __name__, description="Operations on Priorities")

@blp.route("/priority")
class PriorityList(ResourceModel): 
    @is_logged_in
    @blp.response(200, TaskFieldsResponseSchema(many=True))
    def get(self):
        priority = Priority.query.filter(Priority.id.in_(VALID_TYPE_IDS)).all()
        return priority

@blp.route("/priority/<int:id>")
class PriorityId(ResourceModel):
    @is_logged_in
    @blp.response(200, TaskFieldsResponseSchema)
    def get(self, id):
        if id not in VALID_TYPE_IDS:
            return {"message": "Tipo inválido."}, 400

        obj = Priority.query.get_or_404(id)
        return obj, 200

