from app import db

from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

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
    currentNode = db.Column(db.String(15), nullable=False, default="100")
    startedAt = db.Column(db.DateTime, default=datetime.now)
    nextNode = db.Column(JSON, nullable=False)
    updatedAt = db.Column(db.DateTime, default=datetime.now)
    isActive = db.Column(db.Boolean, default=True)

    def __init__(self, nextNode):
        if isinstance(nextNode, str):
            self.nextNode = [nextNode]
            
        elif isinstance(nextNode, list) and all(isinstance(item, str) for item in nextNode):
            if len(nextNode) >= 2:
                self.nextNode = nextNode
                
            else:
                raise ValueError("List must contain at least 2 strings.")
            
        else:
            raise ValueError("Data must be a string or a list of 2 or more strings.")