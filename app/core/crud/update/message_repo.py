from app.models.orm.databases import LastMessageModel
# from app.models.database.db import db
from app import db

class MessageRepository:
    @staticmethod
    def by_phone(phone_number: str, content: str, isRegistered: bool):
        """Updates LastMessageModel entries for the specified phone_number. The update occurs only if isRegistered is False; otherwise, the entries remain unchanged.
        
        :param phone_number: String variable used to update LastMessageModel with the phone_number from which the inbound message originated.
        :param content: String variable to update LastMessageModel with the inbound message.
        :param isRegistered: Boolean variable to discern whether the to update LastMessageModel.
        
        .. versionchanged:: 1.2
        """
        if not isRegistered:
            #lastMessage = LastMessageModel(phone_number=phone_number, content=content)
            #row = MessagesModel.query.filter_by(phone_number=phone_number).first()
            lastMessage = LastMessageModel.query.filter_by(phone_number=phone_number).first()
            lastMessage.content = content
            db.session.add(lastMessage)
            db.session.commit()
