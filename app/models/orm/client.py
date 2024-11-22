from app import db
from datetime import datetime

class ColumnNames:
    NAME = "name"
    NUMBER = "phone_number"
    STATUS = "status"
    CREATED_AT = "created_at"
    LASTORDER_ID= "lastOrder_id"
    LASTORDER_ON= "lastOrder_on"

class ClientModel(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    phone_number = db.Column(db.String(15), unique=False, nullable=False)
    status = db.Column(db.Text, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    last_interaction = db.Column(db.DateTime, default=datetime.now)
    lastOrder_id = db.Column(db.Integer, nullable=True)
    lastOrder_on = db.Column(db.DateTime, nullable=True)
