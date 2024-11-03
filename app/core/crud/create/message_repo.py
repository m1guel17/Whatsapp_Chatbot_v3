# from app.models.orm.databases import MessagesModel
from app.models.orm.message import MessagesModel
# from app.models.orm.databases import LastMessageModel
from app.models.orm.message import LastMessageModel
from app import db

from datetime import datetime

class MessageRepository:
    @staticmethod
    def new(phone_number: str, content: str):
        """Stores client data into database.
        
        :param phone_number: String variable used to store in MessagesModel the phone_number from which the inbound message originated.
        :param content: String variable for message content 

        .. versionchanged:: 0.2
        """
        sentAt = datetime.utcnow()
        
        messageInstance = MessagesModel(phone_number=phone_number, content=content, chat=1, sent_at=sentAt)
        lastmessageInstance = LastMessageModel(phone_number=phone_number, content=content, sent_at=sentAt)
        
        db.session.add_all([messageInstance, lastmessageInstance])
        db.session.commit()
        