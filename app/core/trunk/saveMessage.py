from app.services import Client
# from app.services import Message
# from app.services.message import Message
# from app.services.client import Client

import time

def saveText(content, phone_number):
    if Client.isNew(phone_number):
        Client.registerClient(phone_number)
        
    else:
        clientInstance = Client.get_one(phone_number)
        
    
    # time.sleep(10)
    #Message.register(phone_number, content)
    
    if "status" in content:
        # Message.update_by_phone(phone_number, "changed status")
        Client.update_status(phone_number, "client")
    
    elif "id" in content:
        # Message.update_by_phone(phone_number, "changed id")
        Client.update_lastOrder_id(phone_number, 12089)