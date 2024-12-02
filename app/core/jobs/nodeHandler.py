import json
import os


def get_response_from_node(node):
    current_dir = os.path.dirname(__file__)
    json_path = os.path.join(current_dir, '..', 'json', 'chatflowv1.json')
    json_path = os.path.normpath(json_path)
    with open(json_path, 'r', encoding='utf-8') as f:
        CHATFLOW = json.load(f)
        
    CHATFLOW = CHATFLOW["nodes"].get(node)
    
    if CHATFLOW["type"] == "text":
        nodetype = CHATFLOW["type"]
        nextNode = CHATFLOW["next"]["default"]
        payload = CHATFLOW["text"]["body"]
        # payload = {
        #     "type": CHATFLOW["type"],
        #     "preview_url": CHATFLOW["text"]["preview_url"],
        #     "body": CHATFLOW["text"]["body"]
        #     }
    else:
        nodetype = "!text"
        nextNode = "100"
        payload = "not text back to 100"
        
        # nextNode = "!text"

        # buttons = CHATFLOW["interactive"]["action"]["buttons"]
        # payload = {
        #     "type": "interactive",
        #     "body": CHATFLOW["interactive"]["body"]["text"],
        #     "buttons": [btn["reply"]["title"] for btn in buttons]
        # }
    
    return nodetype, nextNode, payload