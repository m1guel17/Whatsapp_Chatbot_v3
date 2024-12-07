from app import db

from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

class ColumnNames:
    FUNCNAME = "funcName"
    PROPERTY = "property"
    LOG_CONTENT = "logContent"
    EXEC_AT = "executedAt"
    EXEC_BY = "executedBy"
    
class Status:
    ACTIVE = "active"
    CLOSED = "closed"

class ConversationModel(db.Model):
    __tablename__ = 'conversations'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    status = db.Column(db.String(15), unique=False, nullable=False, default="OPEN")
    nextNode = db.Column(db.String(15), nullable=True, default="100")
    expected = db.Column(db.String(15), nullable=False, default="text")
    action = db.Column(db.String(15), nullable=False, default="")
    startedAt = db.Column(db.DateTime, default=datetime.now)
    updatedAt = db.Column(db.DateTime, default=datetime.now)
    isActive = db.Column(db.Boolean, default=True)
