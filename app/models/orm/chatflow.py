from app import db

from datetime import datetime

class ChatflowModel(db.Model):
    __tablename__ = 'chatflows'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    description = db.Column(db.Text)
    createdAt = db.Column(db.DateTime, default=datetime.now)
    createdBy = db.Column(db.String(15), default="Admin")
    modifiedOn = db.Column(db.DateTime, default=datetime.now)
    modifiedBy = db.Column(db.String(15), default="Admin")
    isActive = db.Column(db.Boolean, default=True)

    nodes = db.relationship('ChatFlowNode', back_populates='chatflow')