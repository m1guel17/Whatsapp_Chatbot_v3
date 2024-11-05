from app.models.orm.message import MessagesModel
from app.models.orm.message import LastMessageModel
from app import db

from datetime import datetime

class MessageRepository:
    @staticmethod
    def by_phone(phone_number: str, content: str):
        """Updates LastMessageModel entries for the specified phone_number. The update occurs only if isRegistered is False; otherwise, the entries remain unchanged.
        
        :param phone_number: String variable used to update LastMessageModel with the phone_number from which the inbound message originated.
        :param content: String variable to update LastMessageModel with the inbound message.
        
        .. versionchanged:: 1.5
        """
        sentAt = datetime.utcnow()
        
        lastChat_ = MessagesModel.query.filter_by(phone_number=phone_number).order_by(MessagesModel.id.desc()).first()
        
        MessageInstance = MessagesModel(phone_number=phone_number, content=content, sent_at=sentAt, chat=lastChat_.chat + 1)
        
        lastMessageInstance = LastMessageModel.query.filter_by(phone_number=phone_number).first()
        lastMessageInstance.content = content
        lastMessageInstance.sent_at = sentAt
        lastMessageInstance.status = "pending response"
        
        db.session.add_all([MessageInstance,lastMessageInstance])
        db.session.commit()
    
    @staticmethod
    def in_and_out_msg(phone_number: str, status: str):
        """Updates LastMessageModel entries for the specified phone_number. The update occurs only if isRegistered is False; otherwise, the entries remain unchanged.
        
        :param phone_number: String variable used to update LastMessageModel with the phone_number from which the inbound message originated.
        :param content: String variable to update LastMessageModel with the inbound message.
        
        .. versionchanged:: 0.2
        """
        sentAt = datetime.utcnow()
        
        lastMessageInstance = LastMessageModel.query.filter_by(phone_number=phone_number).first()
        lastMessageInstance.sent_at = sentAt
        lastMessageInstance.status = status
        
        db.session.add(lastMessageInstance)
        db.session.commit()