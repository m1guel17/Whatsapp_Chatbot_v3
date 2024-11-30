from app import db
from datetime import datetime

class ColumnNames:
    NUMBER = "phone_number"
    MESSAGE = "content"
    CHAT = "chat"
    SENT_AT = "sent_at"

class MessagesModel(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), unique=False, nullable=False)
    content = db.Column(db.Text, nullable=False)
    chat = db.Column(db.Integer, nullable=True)
    sent_at = db.Column(db.DateTime, default=datetime.now)
    isActive = db.Column(db.Boolean, default=True)

class LastMessageModel(db.Model):
    __tablename__ = 'messagesLast'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.Text, nullable=False)