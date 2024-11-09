from config import db


class Type(db.Model):
    __tablename__ = "types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    team_users = db.relationship("TeamUser", backref="type", lazy=True)
