from app.interfaces.api.whatsapp_api import send_response
from app.interfaces.generator.msg.json_format import plain_txt
from app.stack.constant.messages_list import welcome_msg, payment_msg
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
    	
        if clientInstance.status == "intention of payment":
            send_response(plain_txt(phone_number, "Hemos recibido tu información en unos minutos alguien se comunicará contigo, muchas gracias"))
            Message.update_by_phone(phone_number, content, "Check email")
            
        if "pagar" in content.lower():
            send_response(plain_txt(phone_number, payment_msg))
            Client.update_status(phone_number, "intention of payment")
        
            