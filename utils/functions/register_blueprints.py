from auth.google_auth import blp as GoogleAuthBlueprint
from auth.generate_cookie import blp as TestCookieBluePrint
from resources.user import blp as UserBluePrint
from resources.team import blp as TeamBluePrint
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
    api.register_blueprint(TestCookieBluePrint)
    api.register_blueprint(UserBluePrint)
    api.register_blueprint(TeamBluePrint)
