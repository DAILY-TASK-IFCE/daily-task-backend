from app import db

class Daily(db.Model):
    __tablename__ = 'dailies'
    id = db.Column(db.Integer, primary_key=True)
    user_team_id = db.Column(db.Integer, db.ForeignKey('user_teams.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    items = db.relationship('Item', backref='daily', lazy=True)

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=True)
    daily_id = db.Column(db.Integer, db.ForeignKey('dailies.id'), nullable=False)

