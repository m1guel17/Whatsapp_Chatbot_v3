from app import db
from datetime import datetime

class ColumnNames:
    CONTENT = "content"
    SENT_AT = "sent_at"

class RawModel(db.Model):
    __tablename__ = 'raw'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)