from config import db

class FormItem(db.Model):
    __tablename__ = 'form_items'
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    user_form_items = db.relationship('UserFormItem', backref='form_items', lazy=True) 

