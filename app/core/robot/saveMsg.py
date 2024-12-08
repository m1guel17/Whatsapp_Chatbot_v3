from app.interfaces.api.whatsapp_api import send_response
from app.interfaces.generator.msg.json_format import plain_txt
# from app.stack.constant.messages_list import welcome_msg, payment_msg
from app.core.jobs.closeDeal import notify_owner_about_deal
from app.services import Message
from app.services import Customer

import os
import json

def load_json():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "chatflow.json")
    
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)



def saveTextNew(phone_number: str, content: str): # chatflow mock, pending improvement
    if Customer.isNew(phone_number):  # checks if number is new client or not
        Message.registerMsgs(phone_number)#, content)
        Customer.registerClient(phone_number)
    else:
        chatFlow = load_json()
        
        clientStatus = Customer.get_by(phone_number).status
        
        filtered_nodes = {node_id: node for node_id, node in chatFlow["nodes"].items() if node.get("status") == clientStatus}
        
        
        