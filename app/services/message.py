from app.core.crud.message_repository import MessageRepository
from app.models.orm.message import MessageModel

class Message:
    @staticmethod
    def get_all():
        return MessageRepository.get_all_messages()

    @staticmethod
    def register(phone_number, content):
        message = MessageModel(phone_number=phone_number, content=content)
        MessageRepository.add_message(message)
        return message
    
