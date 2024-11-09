from config import db

class TeamUser(db.Model):
    __tablename__ = 'team_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'), nullable=False)
    tasks = db.relationship('UserTask', backref='team_users', lazy=True)
    groups = db.relationship('UserGroup', backref='team_users', lazy=True)
    user_form_items = db.relationship('UserFormItem', backref='team_users', lazy=True)

