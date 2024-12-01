from app import db
from datetime import datetime

class ColumnNames:
    NAME = "name"
    NUMBER = "phone_number"
    STATUS = "status"
    CREATED_AT = "created_at"
    LASTORDER_ID= "lastOrder_id"
    LASTORDER_ON= "lastOrder_on"

class STATUS:
    ACTIVE = "active"
    INACTIVE = "inactive"
    BLOCKED = "blocked"

class CustomerModel(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    phone_number = db.Column(db.String(15), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=True)
    status = db.Column(db.Text, unique=False, nullable=False, default="active")
    created_at = db.Column(db.DateTime, default=datetime.now)
    last_interaction = db.Column(db.DateTime, default=datetime.now)
    isActive = db.Column(db.Boolean, default=True)
    
    conversations = db.relationship('ConversationModel', backref='customer', lazy=True)
