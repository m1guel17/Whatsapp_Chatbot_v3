from app.interfaces.api.whatsapp_api import send_response
from app.interfaces.generator.msg.json_format import plain_txt
from app.core.robot.messages_list import welcome_msg
from app.services import Message
from app.services import Client

def saveText(phone_number: str, content: str):
    if Client.isNew(phone_number):  # checks if number is new client or not
        Message.registerMsgs(phone_number, content)
        Client.registerClient(phone_number)
        send_response(plain_txt(phone_number, welcome_msg))
        
    else:
        clientInstance = Client.get_one(phone_number)
        Message.update_by_phone(phone_number, content)

    
        if "status" in content:
            send_response(plain_txt(phone_number, "status changed"))
            Client.update_status(phone_number, "client")
            
        elif "id" in content:
            send_response(plain_txt(phone_number, "id generated"))
            Client.update_lastOrder_id(phone_number, 12089)