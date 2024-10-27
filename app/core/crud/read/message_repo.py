from app.models.orm.message import MessagesModel
from app.models.orm.message import ColumnNames
from app.models.database.db import db
from sqlalchemy import desc

class MessageRepository:
    @staticmethod
    def get_all_messages():
        return MessagesModel.query.all()
    
    @staticmethod
    def get_last_message():#phone_number
        column = getattr(MessagesModel, ColumnNames.NUMBER)
        #return MessagesModel.query.filter_by(column=phone_number).order_by(desc(MessagesModel.id)).first()
        return MessagesModel.query.order_by(desc(MessagesModel.id)).first()