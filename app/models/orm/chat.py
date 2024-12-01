from app import db

from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

class STATUS:
    OPEN = "open"
    CLOSE = "closed"
    DROPED = "droped"

class ConversationModel(db.Model):
    __tablename__ = 'conversations'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    status = db.Column(db.String(15), unique=False, nullable=False, default="open")
    currentNodeID = db.Column(db.String(15), nullable=False, default="100")
    startedAt = db.Column(db.DateTime, default=datetime.now)
    nextNode = db.Column(db.String(15), nullable=True)
    updatedAt = db.Column(db.DateTime, default=datetime.now)
    isActive = db.Column(db.Boolean, default=True)
