from app.interfaces.api.whatsapp_api import send_response
from app.interfaces.generator.msg.json_format import plain_txt
# from app.stack.constant.messages_list import welcome_msg, payment_msg
from app.core.jobs.closeDeal import notify_owner_about_deal
from app.services import Message
from app.services import Client

import os

def saveText(phone_number: str, content: str):
    if Client.isNew(phone_number):  # checks if number is new client or not
        Message.registerMsgs(phone_number, content)
        Client.registerClient(phone_number)
        send_response(plain_txt(phone_number, "welcome"))
        
    else:
        clientInstance = Client.get_one(phone_number)
    	
        if clientInstance.status == "intention of payment":
            send_response(plain_txt(phone_number, "Information received"))
            Message.update_by_phone(phone_number, content, "Check email")
            
        if "pagar" in content.lower():
            send_response(plain_txt(phone_number, "payment"))
            Client.update_status(phone_number, "intention of payment")
        
        if "email" in content.lower():
            Message.update_by_phone(phone_number, content, "Check email")
            notify_owner_about_deal("John Doe", "123456789", os.environ.get('RECEIVER_EMAIL')) # this is jsut for testing
        
        else:
            if clientInstance.status != "intention of payment":
                Message.update_by_phone(phone_number, content)
            
            