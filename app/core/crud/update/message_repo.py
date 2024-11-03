from app.models.orm.databases import MessagesModel
from app.models.orm.databases import LastMessageModel
from app import db

from datetime import datetime

class MessageRepository:
    @staticmethod
    def by_phone(phone_number: str, content: str):
        """Updates LastMessageModel entries for the specified phone_number. The update occurs only if isRegistered is False; otherwise, the entries remain unchanged.
        
        :param phone_number: String variable used to update LastMessageModel with the phone_number from which the inbound message originated.
        :param content: String variable to update LastMessageModel with the inbound message.
        :param isRegistered: Boolean variable to discern whether the to update LastMessageModel.
        
        .. versionchanged:: 1.3
        """
        sentAt = datetime.utcnow()
        #parsed_sentAt = datetime.strptime(sentAt, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %I:%M:%S %p")
        
        lastMessageInstance = LastMessageModel.query.filter_by(phone_number=phone_number).first()
        lastMessageInstance.content = content
        lastMessageInstance.sent_at = sentAt #parsed_sentAt
        
        db.session.add(lastMessageInstance)
        db.session.commit()
        
        MessageInstance = MessagesModel(phone_number=phone_number, content=content, sent_at=sentAt)
        db.session.add(MessageInstance)
        db.session.commit()