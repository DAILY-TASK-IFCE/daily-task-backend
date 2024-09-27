from config import db

class Daily(db.Model):
    __tablename__ = 'dailies'
    id = db.Column(db.Integer, primary_key=True)
    user_team_id = db.Column(db.Integer, db.ForeignKey('user_teams.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    daily_limit_time_id = db.Column(db.Integer, db.ForeignKey('daily_limit_time.id'), nullable=True)
    items = db.relationship('Item', backref='daily', lazy=True)

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=True)
    daily_id = db.Column(db.Integer, db.ForeignKey('dailies.id'), nullable=False)

class DailyLimitTime(db.Model):
    __tablename__ = 'daily_limit_time'
    
    id = db.Column(db.Integer, primary_key=True)
    time_limit = db.Column(db.Time, nullable=False)
