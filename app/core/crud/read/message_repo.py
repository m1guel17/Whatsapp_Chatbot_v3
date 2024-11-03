from app.models.orm.databases import MessagesModel
from app.models.orm.databases import LastMessageModel
from app import db

class MessageRepository:
    @staticmethod
    def isNew(phone_number: str) -> bool:
        """Gets the first instace from a phone_number in MessagesModel.
        
        :param phone_number: String variable used to check in MessagesModel if the client with phone_number is registered.
        
        .. versionchanged:: 1.1
        """
        return MessagesModel.query.filter_by(phone_number=phone_number).first() is None

    @staticmethod
    def get_all():
        """Gets all the rows in MessagesModel.
        
        .. versionchanged:: 0.1
        """
        return MessagesModel.query.all()
    
    @staticmethod
    def fetch_last(phone_number: str):
        """Gets all the rows in LastMessageModel.
        
        .. versionchanged:: 0.1
        """
        return LastMessageModel.query.all()