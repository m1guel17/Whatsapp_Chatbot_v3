import json
import os


def get_response_from_node(node):
    current_dir = os.path.dirname(__file__)
    json_path = os.path.join(current_dir, '..', 'json', 'chatflowv2.json')
    json_path = os.path.normpath(json_path)
    with open(json_path, 'r', encoding='utf-8') as f:
        chatflowObject = json.load(f)
        
    nodeObject = chatflowObject["nodes"].get(node)
    
    nextNode = nodeObject["next"]["default"]
    payload = nodeObject["payload"]
    
    
    if payload["type"] == "text":
        nodetype = payload["type"]
        # payload = {
        #     "type": CHATFLOW["type"],
        #     "preview_url": CHATFLOW["text"]["preview_url"],
        #     "body": CHATFLOW["text"]["body"]
        #     }
    else:
        nodetype = "!text"
        nextNode = "100"
        payload = {
                "type": "text",
                "text": {
                    "preview_url": False,
                    "body": "not text, back to 100"
                    }
                }
        
        # nextNode = "!text"

        # buttons = CHATFLOW["interactive"]["action"]["buttons"]
        # payload = {
        #     "type": "interactive",
        #     "body": CHATFLOW["interactive"]["body"]["text"],
        #     "buttons": [btn["reply"]["title"] for btn in buttons]
        # }
    
    return nodetype, nextNode, payload