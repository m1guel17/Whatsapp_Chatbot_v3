from app.models.orm.message import MessagesModel
from app.models.orm.message import LastMessageModel
from app.models.database.db import db

class MessageRepository:
    @staticmethod
    def add_message(message, isNew: bool):
        """Add the inbound message to both MessagesMode.
        
        :param message: Instance created from inbound message, contains phone_number and content.
        :param isNew: Boolean variable to discern whether the message instance should be assigned the same chat id or start at 1.

        .. versionchanged:: 1.4
        """
        if isNew:
            message.chat = 1
            db.session.add(message)
            db.session.commit()
            
            message_ = LastMessageModel(phone_number=message.phone_number, content=message.content)
            db.session.add(message_)
            db.session.commit()
            
        else:
            #row = MessagesModel.query.filter_by(phone_number=message.phone_number).first()
            row = MessagesModel.query.filter_by(phone_number=message.phone_number).first()
            message.chat = row.chat + 1
            db.session.add(message)
            db.session.commit()
            
            row_ = LastMessageModel.query.filter_by(phone_number=message.phone_number).first()
            row_.content = message.content
            db.session.commit()
        