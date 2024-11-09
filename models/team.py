from config import db


class Team(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    users = db.relationship("TeamUser", backref="team", lazy=True)
    invites = db.relationship("Invite", backref="team", lazy=True)
    form_items = db.relationship("FormItem", backref="team", lazy=True)
    groups = db.relationship("Group", backref="team", lazy=True)
    daily_limit_time = db.relationship("DailyLimitTime", backref="team", lazy=True)
