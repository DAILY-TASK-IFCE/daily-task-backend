from config import db

class DailyLimitTime(db.Model):
    __tablename__ = 'daily_limit_time'
    
    id = db.Column(db.Integer, primary_key=True)
    time_limit = db.Column(db.Time, nullable=False)
