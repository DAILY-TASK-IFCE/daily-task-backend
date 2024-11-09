from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.task_group import (
    TaskGroupQueryParamsSchema,
    TaskGroupResponseSchema,
    TaskGroupParamsSchema,
)
from models.task_group import TaskGroup
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query

blp = Blueprint("TaskGroups", __name__, description="Operations on TaskGroups")


@blp.route("/task_group")
class TaskGroupList(ResourceModel):
    @is_logged_in
    @blp.arguments(TaskGroupQueryParamsSchema, location="query")
    @blp.response(200, TaskGroupResponseSchema(many=True))
    def get(self, args):
        query = filter_query(TaskGroup, args)
        task_groups = query.all()
        return task_groups

    @is_logged_in
    @handle_exceptions
    @blp.arguments(TaskGroupParamsSchema)
    @blp.response(201)
    def post(self, new_task_data):
        new_task = TaskGroup(**new_task_data)
        self.save_data(new_task)
        return {"message": "Task adicionada com sucesso a um grupo"}, 201


@blp.route("/task_group/<int:id>")
class TaskGroupId(ResourceModel):
    @is_logged_in
    @blp.response(200, TaskGroupResponseSchema)
    def get(self, id):
        task_group = TaskGroup.query.get_or_404(id)
        return task_group, 200

    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        task_group = TaskGroup.query.get_or_404(id)
        self.delete_data(task_group)
        return {"message": "Task removida com sucesso de um grupo"}, 200
