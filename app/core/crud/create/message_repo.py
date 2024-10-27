from app.models.database.db import db

class MessageRepository:
    @staticmethod
    def add_message(message):
        db.session.add(message)
        db.session.commit()