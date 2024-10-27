from app.models.orm.message import MessageModel
from app.models.database.db import db

class MessageRepository:
    @staticmethod
    def get_all_messages():
        return MessageModel.query.all()
    
    @staticmethod
    def add_message(message):
        db.session.add(message)
        db.session.commit()