from utils.functions.nest_item import nest_items
from utils.functions.nest_task import nest_tasks
from utils.functions.nest_group import nest_groups
from utils.functions.nest_team import nest_teams
from utils.functions.nest_team_user import nest_team_user, nest_team_users
from utils.functions.nest_user_form_item import nest_user_form_items
def add_nested_params_to_list(objs, params):
    return [add_nested_params(obj, params) for obj in objs]

def add_nested_params(obj, params):
    nest_funcs = {
        "tasks": nest_tasks,
        "items": nest_items,
        "groups": nest_groups,
        "teams": nest_teams,
        "team_users": nest_team_users,
        "team_user": nest_team_user,
        "user_form_items": nest_user_form_items
    }
    obj_dict = obj.__dict__.copy()
    for attr in params:
        if (attr in nest_funcs) and (attr in obj_dict):
            obj_dict[attr] = nest_funcs[attr](obj)
    return obj_dict


