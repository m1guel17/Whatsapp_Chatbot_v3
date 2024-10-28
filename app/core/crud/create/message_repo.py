from app.models.orm.message import LastMessageModel
from app.models.database.db import db

class MessageRepository:
    @staticmethod
    def add_message(message, isNew: bool):
        """Add the inbound message to both MessagesMode.
        
        :param message: Instance created from inbound message, contains phone_number and content.
        :param isNew: Boolean variable to discern whether the message instance should be assigned the same chat id or start at 1.

        .. versionchanged:: 1.2
        """
        if isNew:
            message.chat = 1
        else:
            message.chat = message.chat + 1
        
        db.session.add(message)
        db.session.commit()
        