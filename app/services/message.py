from app.core.crud.create.message_repo import MessageRepository as msgCreate
from app.core.crud.read.message_repo import  MessageRepository as msgRead
from app.core.crud.update.message_repo import MessageRepository as msgUpdate
from app.models.orm.message import MessagesModel

class Message:
    @staticmethod
    def register(phone_number, content):
        message = MessagesModel(phone_number=phone_number, content=content)
        msgCreate.add_message(message)
    
    @staticmethod
    def get_all():
        return msgRead.get_all_messages()

    @staticmethod
    def get_last():
        return msgRead.get_last_message()

    @staticmethod
    def update_by_phone(phone_number):
        msgUpdate.by_phone(phone_number)