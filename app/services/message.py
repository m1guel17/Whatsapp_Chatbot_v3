from app.core.crud.create.message_repo import MessageRepository as msgCreate
from app.core.crud.read.message_repo import  MessageRepository as msgRead
from app.core.crud.update.message_repo import MessageRepository as msgUpdate

"""
    Services - Message script to handle message operations
    ----------------------------------------------------------------------------
    >Created: @2024-10-26
    >Last_modified: 2024-10-27
    >Author: Miguel
"""

class Message:
    # ================================= CREATE =================================
    @staticmethod
    def register(phone_number: str, content: str):
        isNewEntry = Message.isNew(phone_number)
        
        #msgCreate.add_message(message, isNewEntry)
        msgCreate.add_message(phone_number, content, isNewEntry)
        Message.update_by_phone(phone_number, content, isNewEntry)
    
    # ================================== READ ==================================
    @staticmethod
    def isNew(phone_number: str):
        return msgRead.check_if_isNew(phone_number)

    @staticmethod
    def get_all():
        return msgRead.get_all_messages()
    
    @staticmethod
    def fetch_last_msgs():
        return msgRead.fetch_last_msgs_from_clients()

    # ================================= UPDATE =================================
    @staticmethod
    def update_by_phone(phone_number: str, content: str):
        msgUpdate.by_phone(phone_number, content, Message.isNew(phone_number))
    
    # ================================= DELETE =================================