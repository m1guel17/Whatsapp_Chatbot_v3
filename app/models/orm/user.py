from app.models.database.db import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    status = db.Column(db.String(15), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
