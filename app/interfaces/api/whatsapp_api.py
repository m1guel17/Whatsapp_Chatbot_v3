from app.stack.constant.whatsapp import WHATSAPP_API
from app.services import Message

from flask import json
import http.client

"""
    API - whatsapp_api script to send response to client based on json message
    ----------------------------------------------------------------------------
    >Created: 2024-10-27
    >Last_modified: 2024-11-01
    >Author: Miguel
"""

def send_response(data):
    data_ = json.dumps(data)

    headers = {
        "Content-Type": "application/json",
        "Authorization": WHATSAPP_API.TOKEN
    }
    connection = http.client.HTTPSConnection(WHATSAPP_API.URL)    
    try:
        connection.request("POST", WHATSAPP_API.REQUEST, data_, headers)
        response = connection.getresponse()
        print(response.status, response.reason)
        Message.update_in_and_out(data["to"], "response sent")
        
    except Exception as e:
        print(e)
        
    finally:
        connection.close()
        