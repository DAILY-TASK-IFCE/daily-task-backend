from config import db

class Daily(db.Model):
    __tablename__ = 'dailies'
    id = db.Column(db.Integer, primary_key=True)
    user_team_id = db.Column(db.Integer, db.ForeignKey('user_teams.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    daily_limit_time_id = db.Column(db.Integer, db.ForeignKey('daily_limit_time.id'), nullable=True)
    items = db.relationship('Item', backref='daily', lazy=True)

