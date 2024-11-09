from models.user_form_item import UserFormItem

def nest_user_form_items(obj):
    return [UserFormItem.query.get(user_form_item_obj.user_form_item_id) for user_form_item_obj in obj.user_form_items]
