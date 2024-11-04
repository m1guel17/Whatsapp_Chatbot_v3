from app.interfaces.crud.create.message_repo import MessageRepository as msgCreate
from app.interfaces.crud.read.message_repo import MessageRepository as msgRead
from app.interfaces.crud.update.message_repo import MessageRepository as msgUpdate

"""
    Services - Message script to handle message operations
    ----------------------------------------------------------------------------
    >Created: 2024-10-26
    >Last_modified: 2024-11-02
    >Author: Miguel
"""

class Message:
    # ================================= CREATE =================================
    @staticmethod
    def registerMsgs(phone_number: str, content: str):
        msgCreate.new(phone_number, content)
    
    # ================================== READ ==================================
    @staticmethod
    def isNew(phone_number: str):
        return msgRead.isNew(phone_number)

    @staticmethod
    def get_all():
        return msgRead.get_all()
    
    @staticmethod
    def fetch_last_msgs():
        return msgRead.fetch_last()

    # ================================= UPDATE =================================
    @staticmethod
    def update_by_phone(phone_number: str, content: str):
        msgUpdate.by_phone(phone_number, content)
        
    @staticmethod
    def update_in_and_out(phone_number: str, status: str):
        msgUpdate.in_and_out_msg(phone_number, status)
        
    # ================================= DELETE =================================
    
    