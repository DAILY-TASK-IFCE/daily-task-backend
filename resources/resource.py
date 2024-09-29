from flask.views import MethodView
from config import db


class ResourceModel(MethodView):
    def save_data(self, obj):
        db.session.add(obj)
        db.session.commit()

    def delete_data(self, obj):
        db.session.delete(obj)
        db.session.commit()
