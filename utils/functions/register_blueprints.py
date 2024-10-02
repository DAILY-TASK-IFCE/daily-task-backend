from auth.google_auth import blp as GoogleAuthBlueprint
from resources.user import blp as UserBluePrint
from resources.team import blp as TeamBluePrint
from resources.invite import blp as InviteBluePrint
from resources.user_team import blp as UserTeamBluePrint
from resources.group import blp as GroupBluePrint
from resources.type import blp as TypeBluePrint
from resources.status import blp as StatusBluePrint
from resources.priority import blp as PriorityBluePrint
from resources.difficulty import blp as DifficultyBluePrint
from resources.task_type import blp as TaskTypeBluePrint
from resources.task import blp as TaskBluePrint
from resources.user_task import blp as UserTaskBluePrint
from werkzeug.exceptions import UnprocessableEntity

@UserBluePrint.errorhandler(UnprocessableEntity)
def handle_unprocessable_entity_error(error):
    errors = {}

    messages = []
    if error.data:
        errors = error.data.get('messages', {}).get('json', {})
        for field, field_errors in errors.items():
            messages.extend(field_errors)

    if not messages:
        messages = ["Erro de validação desconhecido"]

    return {"messages": messages}, 422

def register_blueprints(api):
    api.register_blueprint(GoogleAuthBlueprint)
    api.register_blueprint(UserBluePrint)
    api.register_blueprint(TeamBluePrint)
    api.register_blueprint(InviteBluePrint)
    api.register_blueprint(UserTeamBluePrint)
    api.register_blueprint(GroupBluePrint)
    api.register_blueprint(TypeBluePrint)
    api.register_blueprint(StatusBluePrint)
    api.register_blueprint(PriorityBluePrint)
    api.register_blueprint(DifficultyBluePrint)
    api.register_blueprint(TaskTypeBluePrint)
    api.register_blueprint(TaskBluePrint)
    api.register_blueprint(UserTaskBluePrint)
