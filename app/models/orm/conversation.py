from app import db

from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

class ColumnNames:
    FUNCNAME = "funcName"
    PROPERTY = "property"
    LOG_CONTENT = "logContent"
    EXEC_AT = "executedAt"
    EXEC_BY = "executedBy"

class ConversationModel(db.Model):
    __tablename__ = 'chats'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer)
    status = db.Column(db.String(15), unique=False, nullable=False, default="OPEN")
    currentNode = db.Column(db.String(15), nullable=False, default="100")
    startedAt = db.Column(db.DateTime, default=datetime.now)
    nextNode = db.Column(db.String(15), nullable=True)
    updatedAt = db.Column(db.DateTime, default=datetime.now)
    isActive = db.Column(db.Boolean, default=True)
