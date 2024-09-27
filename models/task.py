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
    user_teams = db.relationship('UserTask', backref='task', lazy=True)
    groups = db.relationship('TaskGroup', backref='task', lazy=True)

class Status(db.Model):
    __tablename__ = 'statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tasks = db.relationship('Task', backref='status', lazy=True)

class Priority(db.Model):
    __tablename__ = 'priorities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tasks = db.relationship('Task', backref='priority', lazy=True)

class Difficulty(db.Model):
    __tablename__ = 'difficulties'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tasks = db.relationship('Task', backref='difficulty', lazy=True)

class TaskType(db.Model):
    __tablename__ = 'task_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tasks = db.relationship('Task', backref='task_type', lazy=True)

class TaskGroup(db.Model):
    __tablename__ = 'task_groups'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
class UserTask(db.Model):
    __tablename__ = 'user_tasks'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    user_team_id = db.Column(db.Integer, db.ForeignKey('user_teams.id'), nullable=False)
    
