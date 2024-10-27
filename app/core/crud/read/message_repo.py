from app.models.orm.message import MessagesModel
from app.models.orm.message import ColumnNames
from app.models.database.db import db

class MessageRepository:
    @staticmethod
    def get_all_messages():
        return MessagesModel.query.all()
    
    @staticmethod
    def get_last_message():#phone_number
        column = getattr(MessagesModel, ColumnNames.NUMBER)
        #return MessagesModel.query.filter_by(column=phone_number).order_by(desc(MessagesModel.id)).first()
        last_row = MessagesModel.query.order_by(MessagesModel.id.desc()).first()
        if last_row is not None:
            return last_row
        else:
            dummy = MessagesModel(id = 1, phone_number = "xxx-xxx-xxx", content = "message", sent_at = "date")
        
        return dummy