from app import db

from datetime import datetime

# class ColumnNames:
#     NUMBER = "phone_number"
#     MESSAGE = "content"
#     CHAT = "chat"
   
class ClientModel(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    phone_number = db.Column(db.String(15), unique=False, nullable=False)
    status = db.Column(db.Text, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    lastOrder_id = db.Column(db.Integer, nullable=True)
    lastOrder_on = db.Column(db.DateTime, nullable=True)

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(15), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    modified_on = db.Column(db.DateTime, nullable=True)