from config import db

class UserFormItem(db.Model):
    __tablename__ = 'user_form_items'
    id = db.Column(db.Integer, primary_key=True)
    team_user_id = db.Column(db.Integer, db.ForeignKey('team_users.id'), nullable=False)
    form_item_id = db.Column(db.Integer, db.ForeignKey('form_items.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

