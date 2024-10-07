from models.item import Item

def nest_item(obj):
    return [Item.query.get(item_obj.item_id) for item_obj in obj.items]


