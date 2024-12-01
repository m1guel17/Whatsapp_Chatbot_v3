from app import db

from datetime import datetime

class ChatflowNodesModel(db.Model):
    __tablename__ = 'chatflownodes'

    id = db.Column(db.Integer, primary_key=True)
    chatflow_id = db.Column(db.Integer, db.ForeignKey('chatflows.id'))
    node_id = db.Column(db.String(50))  # Corresponds to node IDs in JSON
    node_type = db.Column(db.String(50))  # 'text', 'interactive', etc.
    content = db.Column(db.JSON)  # Stores 'text' or 'interactive' content
    status = db.Column(db.String(50)) # Stores the status
    isActive = db.Column(db.Boolean, default=True)
    
    chatflow = db.relationship('ChatFlow', back_populates='nodes')
    outgoing_transitions = db.relationship('ChatFlowTransition', foreign_keys='ChatFlowTransition.from_node_id', back_populates='from_node')
    incoming_transitions = db.relationship('ChatFlowTransition', foreign_keys='ChatFlowTransition.to_node_id', back_populates='to_node')
