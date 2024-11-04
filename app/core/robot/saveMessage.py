from app.services import Message
from app.services import Client

def saveText(content, phone_number):
    if Client.isNew(phone_number):
        Message.registerMsgs(phone_number, content)
        Client.registerClient(phone_number)
        
    else:
        clientInstance = Client.get_one(phone_number)
        print(clientInstance)
        Message.update_by_phone(phone_number, content)

    
        if "status" in content:
            Message.update_by_phone(phone_number, "changed status")
            Client.update_status(phone_number, "client")
        
        elif "id" in content:
            Message.update_by_phone(phone_number, "changed id")
            Client.update_lastOrder_id(phone_number, 12089)