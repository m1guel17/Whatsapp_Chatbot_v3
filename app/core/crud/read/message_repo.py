from app.models.orm.message import MessagesModel
from app.models.orm.message import LastMessageModel
from app.models.database.db import db

class MessageRepository:
    @staticmethod
    def check_if_isNew(phone_number: str) -> bool:
        """Gets the last message from a phone_number.
        
        :param phone_number: String variable used to check in MessagesModel the client with phone_number is registered.
        
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
    
    @staticmethod
    def get_last_message_():#phone_number # testing
        """Gets all the last messages in MessagesModel from each number. Returns MessagesModel list.
        
        .. versionchanged:: 0.1
        """
        
        #column = getattr(MessagesModel, ColumnNames.NUMBER)
        #return MessagesModel.query.filter_by(column=phone_number).order_by(desc(MessagesModel.id)).first()
        last_row = MessagesModel.query.order_by(MessagesModel.id.desc()).first()
        if last_row is not None:
            return last_row
        else:
            dummy = MessagesModel(id = 1, phone_number = "xxx-xxx-xxx", content = "message", sent_at = "date")
        return dummy