from app.config import WHATSAPP_API
from flask import json
import http.client
import os

def send_response(data):
    data = json.dumps(data)

    headers = {
        "Content-Type": "application/json",
        "Authorization": WHATSAPP_API.TOKEN
    }
    connection = http.client.HTTPSConnection(WHATSAPP_API.URL)    
    try:
        connection.request("POST", WHATSAPP_API.REQUEST, data, headers)
        response = connection.getresponse()
        print(response.status, response.reason)
    except Exception as e:
        print(e)
    finally:
        connection.close()