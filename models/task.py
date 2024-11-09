from config import db

class Task(db.Model):
    __tablename__ = 'tasks' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'), nullable=False)
    priority_id = db.Column(db.Integer, db.ForeignKey('priorities.id'), nullable=False)
    difficulty_id = db.Column(db.Integer, db.ForeignKey('difficulties.id'), nullable=False)
    task_type_id = db.Column(db.Integer, db.ForeignKey('task_types.id'), nullable=False)
    team_users = db.relationship('UserTask', backref='task', lazy=True)
    groups = db.relationship('TaskGroup', backref='task', lazy=True)
   
