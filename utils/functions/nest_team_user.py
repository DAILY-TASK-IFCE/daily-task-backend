from models.team_user import TeamUser

def nest_team_user(obj):
    return TeamUser.query.get_or_404(obj.team_user_id)

def nest_team_users(obj):
    return [TeamUser.query.get(team_user_obj.team_user_id) for team_user_obj in obj.team_users]
