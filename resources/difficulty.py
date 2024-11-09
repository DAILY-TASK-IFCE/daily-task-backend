from flask_smorest import Blueprint
from resources.resource import ResourceModel
from schemas.task_fields import TaskFieldsResponseSchema
from models.task_fields import Difficulty
from utils.decorators.is_logged_in import is_logged_in

VALID_TYPE_IDS = {1, 2, 3}

blp = Blueprint("Difficulty", __name__, description="Operations on Difficulties")


@blp.route("/difficulty")
class DifficultyList(ResourceModel):
    @is_logged_in
    @blp.response(200, TaskFieldsResponseSchema(many=True))
    def get(self):
        difficulty = Difficulty.query.filter(Difficulty.id.in_(VALID_TYPE_IDS)).all()
        return difficulty


@blp.route("/difficulty/<int:id>")
class DifficultyId(ResourceModel):
    @is_logged_in
    @blp.response(200, TaskFieldsResponseSchema)
    def get(self, id):
        if id not in VALID_TYPE_IDS:
            return {"message": "Tipo inválido."}, 400

        obj = Difficulty.query.get_or_404(id)
        return obj, 200
