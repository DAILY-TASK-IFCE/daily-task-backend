from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.user_form_item import UserFormItemQueryParamsSchema, UserFormItemResponseSchema, UserFormItemParamsSchema
from models.user_form_item import UserFormItem
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.update_if_present import update_if_present

blp = Blueprint("UserFormItems", __name__, description="Operations on UserFormItems")

@blp.route("/user_form_item")
class UserFormItemList(ResourceModel): 
    @is_logged_in
    @blp.arguments(UserFormItemQueryParamsSchema, location="query")
    @blp.response(200, UserFormItemResponseSchema(many=True))
    def get(self, args):
        query = filter_query(UserFormItem, args)
        user_form_items = query.all()
        return user_form_items
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(UserFormItemParamsSchema)
    @blp.response(201)
    def post(self, new_user_data):
        new_user = UserFormItem(**new_user_data)
        self.save_data(new_user)
        return {"message": "Item de formulário adicionado com sucesso a um usuário."}, 201

@blp.route("/user_form_item/<int:id>")
class UserFormItemId(ResourceModel):
    @is_logged_in
    @blp.response(200, UserFormItemResponseSchema)
    def get(self, id):
        user_form_item = UserFormItem.query.get_or_404(id)
        return user_form_item, 200
 
    @is_logged_in
    @handle_exceptions
    @blp.arguments(UserFormItemQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        user_form_item = UserFormItem.query.get_or_404(id)
        update_if_present(user_form_item, args)
        self.save_data(user_form_item)
        return {"message": "Item de formulário do usuário editado com sucesso"}, 200   
    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        user_form_item = UserFormItem.query.get_or_404(id)
        self.delete_data(user_form_item)
        return {"message": "Item de formulário removido com sucesso de um usuário."}, 200


