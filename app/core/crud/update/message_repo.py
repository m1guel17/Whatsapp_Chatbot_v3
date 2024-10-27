from app.models.orm.message import MessagesModel
from app.models.database.db import db

class MessageRepository:
    @staticmethod
    def by_phone(phone_number, **kwargs):
        row = MessagesModel.query.filter_by(phone_number=phone_number).first()
        
        for key, value in kwargs.items():
            setattr(row, key, value)
            db.session.commit()