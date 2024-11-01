from app.models.orm.databases import MessagesModel
from app.models.orm.databases import LastMessageModel
# from app.models.database.db import db
from app import db

class MessageRepository:
    @staticmethod
    def check_if_isNew(phone_number: str) -> bool:
        """Gets the last message from a phone_number.
        
        :param phone_number: String variable used to check in MessagesModel if the client with phone_number is registered.
        
        .. versionchanged:: 1.1
        """
        row = MessagesModel.query.filter_by(phone_number=phone_number).first()
        if row is not None:
            return False
        else:
            return True
    
    @staticmethod
    def get_all_messages():
        """Gets all the rows in MessagesModel.
        
        .. versionchanged:: 0.1
        """
        return MessagesModel.query.all()
    
    @staticmethod
    def fetch_last_msgs_from_clients():
        """Gets all the last messages from LastMessageModel.
        
        .. versionchanged:: 1.1
        """
        return LastMessageModel.query.all()
    