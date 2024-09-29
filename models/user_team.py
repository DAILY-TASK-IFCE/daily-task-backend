from config import db

class UserTeam(db.Model):
    __tablename__ = 'user_teams'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'), nullable=False)
    tasks = db.relationship('UserTask', backref='user_teams', lazy=True)
    groups = db.relationship('UserGroup', backref='user_teams', lazy=True)
    user_form_items = db.relationship('UserFormItem', backref='user_teams', lazy=True)

