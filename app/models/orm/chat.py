from app import db

from datetime import datetime

class ColumnNames:
    FUNCNAME = "funcName"
    PROPERTY = "property"
    LOG_CONTENT = "logContent"
    EXEC_AT = "executedAt"
    EXEC_BY = "executedBy"

class ChatModel(db.Model):
    __tablename__ = 'chats'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer)
    status = db.Column(db.String(15), unique=False, nullable=False, default="OPEN")
    startedAt = db.Column(db.DateTime, default=datetime.now)
    updatedAt = db.Column(db.DateTime, default=datetime.now)
    isActive = db.Column(db.Boolean, default=True)

