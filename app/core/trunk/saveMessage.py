from app.services.message import Message
from app.services.client import Client

def saveText(content, phone_number):
    Message.register(phone_number, content)
    Client.register(phone_number)
    
    if content == "status":
        Client.update_status(phone_number, "client")
    
    elif content == "id":
        Client.update_lastOrder_id(phone_number, 12089)