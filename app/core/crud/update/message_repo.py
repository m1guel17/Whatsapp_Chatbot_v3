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
        sentAt = datetime.now()
        parsed_sentAt = datetime.strptime(sentAt, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %I:%M:%S %p")
        
        lastMessageInstance = LastMessageModel.query.filter_by(phone_number=phone_number).first()
        lastMessageInstance.content = content
        lastMessageInstance.sent_at = parsed_sentAt
        
        MessageInstance = MessagesModel(phone_number=phone_number, content=content)
        
        db.session.add_all([MessageInstance, lastMessageInstance])
        db.session.commit()