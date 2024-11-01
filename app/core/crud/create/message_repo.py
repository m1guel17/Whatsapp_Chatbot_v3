from app.models.orm.databases import MessagesModel
from app.models.orm.databases import LastMessageModel
# from app.models.database.db import db
from app import db

from datetime import datetime

class MessageRepository:
    @staticmethod
    def add_message(phone_number: str, content: str, isNew: bool):
        """Add the inbound message to both MessagesMode.
        
        :param phone_number: String variable used to update MessagesModel and LastMessageModel with the phone_number from which the inbound message originated.
        :param content: String variable to update MessagesModel and LastMessageModel with the last inbound message.
        :param isNew: Boolean variable to discern whether the message instance should be assigned the same chat id or start at 1.

        .. versionchanged:: 1.9
        """
        sentAt = datetime.utcnow()
        
        if isNew:
            message = MessagesModel(phone_number=phone_number, content=content, chat=1, sent_at=sentAt)
            message_ = LastMessageModel(phone_number=phone_number, content=content, sent_at=sentAt)
            
            db.session.add_all([message, message_])
            
        else:
            messagelast = MessagesModel.query.filter_by(phone_number=phone_number).order_by(MessagesModel.id.desc()).first()
            message = MessagesModel(phone_number=phone_number, content=content, chat=messagelast.chat+1 , sent_at=sentAt)
            
            message_ = LastMessageModel.query.filter_by(phone_number=phone_number).first()
            message_.content = content
            message_.sent_at = sentAt
            
            db.session.add_all([message, message_])
        
        db.session.commit()