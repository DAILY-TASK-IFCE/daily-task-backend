from models.user_team import UserTeam

def nest_user_team_in_tasks(tasks):
    task_list = [nest_user_team_in_task(task) for task in tasks]
    return task_list

def nest_user_team_in_task(task):
    task_dict = task.__dict__.copy()
    nested_user_tasks = []
    for user_task in task.user_teams:
        nested_user_task = UserTeam.query.get_or_404(user_task.user_team_id)
        nested_user_tasks.append(nested_user_task)
    task_dict['user_teams'] = nested_user_tasks
    return task_dict

