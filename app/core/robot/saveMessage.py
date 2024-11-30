from app.interfaces.api.whatsapp_api import send_response
from app.interfaces.generator.msg.json_format import plain_txt
# from app.stack.constant.messages_list import welcome_msg, payment_msg
from app.core.jobs.closeDeal import notify_owner_about_deal
from app.services import Message
from app.services import Client

import os

def saveText(phone_number: str, content: str): # chatflow mock, pending improvement
    if Client.isNew(phone_number):  # checks if number is new client or not
        Message.registerMsgs(phone_number, content)
        Client.registerClient(phone_number)
        send_response(plain_txt(phone_number, "welcome")) # replace with custom welcome message
        
    else:
        clientStatus = Client.get_one(phone_number).status
        
        match clientStatus:
            case "potential client":
                if "pagar" in content.lower():
                    Message.update_by_phone(phone_number, content, "payment")
                    Client.update_status(phone_number, "intention of payment")
                    send_response(plain_txt(phone_number, "payment"))
                
                else:
                    Message.update_by_phone(phone_number, content)
                    send_response(plain_txt(phone_number, "potential"))
                
            case "intention of payment":
                Message.update_by_phone(phone_number, content)
                Client.update_status(phone_number, "Got info")
                send_response(plain_txt(phone_number, "Information received"))
            case _:
                Message.update_by_phone(phone_number, content)
                send_response(plain_txt(phone_number, f"Client status not configured {clientStatus}"))
                
        if "email" in content.lower():
            Message.update_by_phone(phone_number, content, "Check email")
            Client.update_status(phone_number, "email sent")
            notify_owner_about_deal("John Doe", "123456789", os.environ.get('RECEIVER_EMAIL')) # this is just for testing
            
                