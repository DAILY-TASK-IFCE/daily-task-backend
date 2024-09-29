from config import db

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    users = db.relationship('UserTeam', backref='team', lazy=True)
    invites = db.relationship('Invite', backref='team', lazy=True)
    form_items = db.relationship('FormItem', backref='team', lazy=True)
    groups = db.relationship('Group', backref='team', lazy=True)

class FormItem(db.Model):
    __tablename__ = 'form_items'
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    user_form_items = db.relationship('UserFormItem', backref='form_items', lazy=True) 

class UserFormItem(db.Model):
    __tablename__ = 'user_form_items'
    id = db.Column(db.Integer, primary_key=True)
    user_team_id = db.Column(db.Integer, db.ForeignKey('user_teams.id'), nullable=False)
    form_item_id = db.Column(db.Integer, db.ForeignKey('form_items.id'), nullable=False)
