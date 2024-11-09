from config import db


class Group(db.Model):
    __tablename__ = "groups"
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    users = db.relationship("UserGroup", backref="group", lazy=True)
    tasks = db.relationship("TaskGroup", backref="group", lazy=True)
