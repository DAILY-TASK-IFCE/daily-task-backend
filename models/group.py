from config import db

class Group(db.Model):
    __tablename__ = 'groups'  # Nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    users = db.relationship('UserGroup', backref='group', lazy=True)
    task_groups = db.relationship('TaskGroup', backref='group', lazy=True)

class UserGroup(db.Model):
    __tablename__ = 'user_groups'  # Nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    user_team_id = db.Column(db.Integer, db.ForeignKey('user_teams.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)

