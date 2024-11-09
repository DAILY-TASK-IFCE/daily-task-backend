from models.user_team import UserTeam

def nest_user_team(obj):
    return UserTeam.query.get_or_404(obj.user_team_id)

def nest_user_teams(obj):
    return [UserTeam.query.get(user_team_obj.user_team_id) for user_team_obj in obj.user_teams]
