#from app.core.crud.message_repository import MessageRepository
from app.core.crud.create.message_repo import MessageRepository as msgCreate
from app.core.crud.read.message_repo import  MessageRepository as msgRead
from app.models.orm.message import MessageModel

class Message:
    @staticmethod
    def get_all():
        return msgRead.get_all_messages()

    @staticmethod
    def register(phone_number, content):
        message = MessageModel(phone_number=phone_number, content=content)
        msgCreate.add_message(message)
        return message
    
