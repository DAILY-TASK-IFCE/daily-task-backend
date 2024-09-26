from config import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    photo = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(100), nullable=False)
    teams = db.relationship('UserTeam', backref='user', lazy=True)
    groups = db.relationship('UserGroup', backref='user', lazy=True)
    tasks = db.relationship('UserTask', backref='user', lazy=True)

class UserTeam(db.Model):
    __tablename__ = 'user_teams'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'), nullable=False)

class Type(db.Model):
    __tablename__ = 'types' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_teams = db.relationship('UserTeam', backref='type', lazy=True)

class Invite(db.Model):
    __tablename__ = 'invites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)


