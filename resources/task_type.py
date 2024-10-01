from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.task_fields import TaskFieldsQueryParamsSchema, TaskFieldsResponseSchema, TaskFieldsParamsSchema
from models.task_fields import TaskType
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query

blp = Blueprint("Task Types", __name__, description="Operations on Task Types")

@blp.route("/task_type")
class TaskTypeList(ResourceModel): 
    @is_logged_in
    @blp.arguments(TaskFieldsQueryParamsSchema, location="query")
    @blp.response(200, TaskFieldsResponseSchema(many=True))
    def get(self, args):
        query = filter_query(TaskType, args)
        task_types = query.all()
        return task_types
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(TaskFieldsParamsSchema)
    @blp.response(201)
    def post(self, new_task_type_data):
        if TaskType.query.filter_by(email=new_task_type_data["name"]).first():
            return {"message": "Já existe um tipo de task com esse nome."}, 409

        new_task_type = TaskType(**new_task_type_data)
        self.save_data(new_task_type)
        return {"message": "Tipo de Task criado com sucesso"}, 201

@blp.route("/task_type/<int:id>")
class TaskTypeId(ResourceModel):
    @is_logged_in
    @blp.response(200, TaskFieldsResponseSchema)
    def get(self, id):
        task_type = TaskType.query.get_or_404(id)
        return task_type, 200
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(TaskFieldsQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        task_type = TaskType.query.get_or_404(id)

        for key, value in args.items():
            if value is not None:
                setattr(task_type, key, value)

        self.save_data(task_type)
        return {"message": "Tipo de Task editado com sucesso"}, 200
    
    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        task_type = TaskType.query.get_or_404(id)
        self.delete_data(task_type)
        return {"message": "Tipo de Task deletado com sucesso"}, 200

