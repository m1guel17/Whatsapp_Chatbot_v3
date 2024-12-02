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
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversations.id'), nullable=False)
    # chat = db.Column(db.Integer, nullable=True)
    # phone_number = db.Column(db.String(15), unique=False, nullable=False)
    content = db.Column(db.Text, nullable=False)
    message_type = db.Column(db.String(50), default='text')
    sent_at = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.Text, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    
    conversation = db.relationship('ConversationModel', backref=db.backref('messages', lazy=True))

class LastMessageModel(db.Model):
    __tablename__ = 'messagesLast'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.Text, nullable=False)