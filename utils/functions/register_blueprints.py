from auth.google_auth import blp as GoogleAuthBlueprint
from auth.generate_cookie import blp as TestCookieBluePrint
from resources.user import blp as UserBluePrint
def register_blueprints(api):
    api.register_blueprint(GoogleAuthBlueprint)
    api.register_blueprint(TestCookieBluePrint)
    api.register_blueprint(UserBluePrint)
