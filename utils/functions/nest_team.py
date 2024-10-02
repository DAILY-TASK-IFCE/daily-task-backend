from models.team import Team

def nest_team(obj):
    return [Team.query.get(team_obj.team_id) for team_obj in obj.teams]
