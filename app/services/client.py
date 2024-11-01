from app.core.crud.create.client_repo import ClientRepository as clientCreate
from app.core.crud.read.client_repo import ClientRepository as clientRead
from app.core.crud.update.client_repo import ClientRepository as clientUpdate

"""
    Services - Client script to handle clients operations
    ----------------------------------------------------------------------------
    >Created: 2024-10-27
    >Last_modified: 2024-10-27
    >Author: Miguel
"""

class Client:
    # ================================= CREATE =================================
    @staticmethod
    def registerClient(phone_number: str):        
        clientCreate.new(phone_number)
    
    # ================================== READ ==================================
    @staticmethod
    def isNew(phone_number: str):
        return clientRead.isNew(phone_number)
    
    @staticmethod
    def get_all():
        return clientRead.get_all()
    
    @staticmethod
    def get_one(phone_number: str):
        return clientRead.getByPhone(phone_number)
    
    # ================================= UPDATE =================================
    @staticmethod
    def update_status(phone_number: str, status_update: str):
        clientUpdate.by_phone(phone_number, status=status_update)
    
    @staticmethod
    def update_lastOrder_id(phone_number: str, orderid: int):
        clientUpdate.by_phone(phone_number, lastOrder_id=orderid)
    
    # ================================= DELETE =================================

    