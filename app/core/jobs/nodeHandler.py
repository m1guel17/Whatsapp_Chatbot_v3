import json
import os


def get_response_from_node(node):
    current_dir = os.path.dirname(__file__)
    json_path = os.path.join(current_dir, '..', 'json', 'chatflowv2.json')
    json_path = os.path.normpath(json_path)
    with open(json_path, 'r', encoding='utf-8') as f:
        chatflowObject = json.load(f)
        
    nodeObject = chatflowObject["nodes"].get(node)
    
    type_ = getNodeObjectType(nodeObject, node)
    
    
    
    
    nextNode = nodeObject["next"]["default"]
    payload = nodeObject["payload"]
    
    
    if payload["type"] == "text":
        nodetype = payload["type"]
        
    else:
        nodetype = payload["type"]
        nextNode = "100"
        payload = {
                "type": "text",
				"text": {
					"preview_url": False,
					"body": "FIN"
				    }
                }
    
    return nodetype, nextNode, payload

def getNodeObjectType(Object):
    nodeObjectType = Object["payload"]["type"]
    return nodeObjectType