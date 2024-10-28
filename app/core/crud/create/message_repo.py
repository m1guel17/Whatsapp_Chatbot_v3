from app.models.orm.message import MessagesModel
from app.models.orm.message import LastMessageModel
from app.models.database.db import db

class MessageRepository:
    @staticmethod
    def add_message(phone_number: str, content: str, isNew: bool):
        """Add the inbound message to both MessagesMode.
        
        :param phone_number: String variable used to update MessagesModel and LastMessageModel with the phone_number from which the inbound message originated.
        :param content: String variable to update MessagesModel and LastMessageModel with the last inbound message.
        :param isNew: Boolean variable to discern whether the message instance should be assigned the same chat id or start at 1.

        .. versionchanged:: 1.5
        """
        
        if isNew:
            message = MessagesModel(phone_number=phone_number, content=content, chat=1)
            db.session.add(message)
            db.session.commit()
            
            message_ = LastMessageModel(phone_number=phone_number, content=content)
            db.session.add(message_)
            db.session.commit()
            
        else:
            message = MessagesModel.query.filter_by(phone_number=message.phone_number).order_by(MessagesModel.id.desc()).first()
            message.chat = message.chat + 1
            db.session.add(message)
            db.session.commit()
            
            row_ = LastMessageModel.query.filter_by(phone_number=message.phone_number)
            row_.content = content
            db.session.commit()
        