from app import db

from datetime import datetime

class ColumnNames:
    FUNCNAME = "funcName"
    PROPERTY = "property"
    LOG_CONTENT = "logContent"
    EXEC_AT = "executedAt"
    EXEC_BY = "executedBy"

class LogModel(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    funcName = db.Column(db.String(50), nullable=False)
    property = db.Column(db.String(15), nullable=False)
    logContent = db.Column(db.Text, nullable=False)
    executedAt = db.Column(db.DateTime, default=datetime.now)
    executedBy = db.Column(db.Text, default="Admin") 

