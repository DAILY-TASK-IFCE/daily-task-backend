from models.team import Team

def nest_team_in_users(users):
    user_list = [nest_team_in_user(user) for user in users]
    return user_list

def nest_team_in_user(user):
    user_dict = user.__dict__.copy()
    user_dict.pop('user', None) 
    nested_teams = []
    for team in user.teams:
        nested_team = Team.query.get_or_404(team.team_id)
        nested_teams.append(nested_team)
    user_dict['teams'] = nested_teams
    return user_dict
