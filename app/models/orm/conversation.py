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
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    startedAt = db.Column(db.DateTime, default=datetime.now)
    updatedAt = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.String(15), unique=False, nullable=False, default="open")
    currentNode = db.Column(db.String(10), default="100")
    isActive = db.Column(db.Boolean, default=True)

    #current_node = db.relationship('NodeModel', backref='conversations', foreign_keys=[currentNode_id])
    # customer = db.relationship('CustomerModel', backref='conversations', lazy=True)
    # messages = db.relationship('MessageModel', backref='conversation', lazy=True)
    