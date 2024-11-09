from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.form_item import FormItemQueryParamsSchema, FormItemResponseSchema, FormItemParamsSchema
from models.form_item import FormItem
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.update_if_present import update_if_present

blp = Blueprint("FormItems", __name__, description="Operations on FormItems")

@blp.route("/form_item")
class FormItemList(ResourceModel): 
    @is_logged_in
    @blp.arguments(FormItemQueryParamsSchema, location="query")
    @blp.response(200, FormItemResponseSchema(many=True))
    def get(self, args):
        query = filter_query(FormItem, args)
        items = query.all()
        return items
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(FormItemParamsSchema)
    @blp.response(201)
    def post(self, new_item_data):
        new_item = FormItem(**new_item_data)
        self.save_data(new_item)
        return {"message": "FormItem criado com sucesso"}, 201

@blp.route("/form_item/<int:id>")
class FormItemId(ResourceModel):
    @is_logged_in
    @blp.response(200, FormItemResponseSchema)
    def get(self, id):
        form_item = FormItem.query.get_or_404(id)
        return form_item, 200
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(FormItemQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        form_item = FormItem.query.get_or_404(id)
        update_if_present(form_item, args)
        self.save_data(form_item)
        return {"message": "FormItem editado com sucesso"}, 200
    
    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        form_item = FormItem.query.get_or_404(id)
        self.delete_data(form_item)
        return {"message": "FormItem deletado com sucesso"}, 200

