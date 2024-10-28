from app.models.orm.message import MessagesModel
from app.models.orm.message import LastMessageModel
from app.models.database.db import db

class MessageRepository:
    @staticmethod
    def add_message(message, isNew: bool):
        """Add the inbound message to both MessagesMode.
        
        :param message: Instance created from inbound message, contains phone_number and content.
        :param isNew: Boolean variable to discern whether the message instance should be assigned the same chat id or start at 1.

        .. versionchanged:: 1.3
        """
        if isNew:
            message.chat = 1
            db.session.add(message)
            db.session.commit()
        else:
            row = MessagesModel.query.filter_by(phone_number=message.phone_number).first()
            row.chat = row.chat + 1
            db.session.add(row)
            db.session.commit()
        
        