from app.models.database.db import db
from datetime import datetime

class ColumnNames:
    NUMBER = "phone_number"
    MESSAGE = "content"

class MessagesModel(db.Model):
    __tablename__ = 'messagesLogs'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), unique=False, nullable=False)
    content = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)
