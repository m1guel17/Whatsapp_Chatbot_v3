from app.models.orm.message import MessagesModel
from app.models.orm.message import LastMessageModel
from app import db

from datetime import datetime

class MessageRepository:
    @staticmethod
    def new(phone_number: str, content: str):
        """Stores client data into database.
        
        :param phone_number: String variable used to store in MessagesModel the phone_number from which the inbound message originated.
        :param content: String variable for message content 

        .. versionchanged:: 0.4
        """
        sentAt = datetime.now()
        
        messageInstance = MessagesModel(phone_number=phone_number, content=content, chat=1, sent_at=sentAt, node="100")
        lastmessageInstance = LastMessageModel(phone_number=phone_number, content=content, sent_at=sentAt, status="new chat")
        
        db.session.add_all([messageInstance, lastmessageInstance])
        db.session.commit()
        