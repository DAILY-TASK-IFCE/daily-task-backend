from config import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    photo = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(100), nullable=False)
    teams = db.relationship("TeamUser", backref="user", lazy=True)
