from app.models.orm.databases import MessagesModel
from app.models.orm.databases import LastMessageModel
from app import db

from datetime import datetime

class MessageRepository:
    @staticmethod
    def new(phone_number: str, content: str):
        """Stores client data into database.
        
        :param phone_number: String variable used to store in ClientModel the phone_number from which the inbound message originated.
        :param isNew: Boolean variable to discern whether the client instance should be assigned 'potential client' status.

        .. versionchanged:: 0.1
        """
        sentAt = datetime.utcnow()
        #parsed_sentAt = datetime.strptime(sentAt, "%Y-%m-%d %H:%M:%S")
        #parsed_sentAt2 = datetime.strptime(sentAt, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %I:%M:%S %p")
        
        messageInstance = MessagesModel(phone_number=phone_number, content=content, sent_at=sentAt)
        # messageInstance2 = MessagesModel(phone_number=phone_number, content=content, sent_at=sentAt)
        # messageInstance2 = MessagesModel(phone_number=phone_number, content=content, sent_at=parsed_sentAt2)
        lastmessageInstance = LastMessageModel(phone_number=phone_number, content=content, sent_at=sentAt)
        
        db.session.add_all([messageInstance, lastmessageInstance])
        db.session.commit()
        