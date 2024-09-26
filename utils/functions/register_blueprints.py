from auth.google_auth import blp as GoogleAuthBlueprint
from auth.generate_cookie import blp as TestCookieBluePrint
def register_blueprints(api):
    api.register_blueprint(GoogleAuthBlueprint)
    api.register_blueprint(TestCookieBluePrint)
