from app.core.robot.saveMessage import saveText
from app.services import Raw

from flask import request, jsonify

def receive_message(req_data):
        try:
            req_data = request.get_json()
            Raw.registerRaw(req_data)
            msg_object = req_data.get("entry", [{}])[0].get("changes", [{}])[0].get("value", {}).get("messages", [])
            
            if msg_object:
                messages = msg_object[0]

                if "type" in messages:
                    type = messages["type"]
                    
                    if type == "interactive":
                        interactive_type = messages["interactive"]["type"]

                        if interactive_type == "button_reply":
                            content = messages["interactive"]["button_reply"]["id"]
                            title = messages["interactive"]["button_reply"]["title"]
                            phone_number = messages["from"]
                            saveText(phone_number, content)
                            
                        elif interactive_type == "list_reply":
                            content = messages["interactive"]["list_reply"]["id"]
                            title = messages["interactive"]["list_reply"]["title"]
                            phone_number = messages["from"]
                            saveText(phone_number, content)
                            
                    if "text" in messages:
                        content = messages["text"]["body"]
                        phone_number = messages["from"]
                        saveText(phone_number, content)
            
            
            return jsonify({'message': 'EVENT_RECEIVED'})
        except Exception as e:
            return jsonify({'message': 'EVENT_RECEIVED'})