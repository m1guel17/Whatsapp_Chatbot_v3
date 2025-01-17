
def plain_txt(phone_number, payload):
    msg = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone_number,
        "text": {
            "preview_url": payload["text"]["preview_url"],
            "body": payload["text"]["body"]
        }
    }
    return msg

def plain_txtOld(phone_number, message):
    msg = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone_number,
        "text": {
            "preview_url": False,
            "body": message
        }
    }
    return msg

def button(number, text, footer, options, branch):
    buttons = []
    for i in range(len(options)):
        button_ = {
            "type": "reply",
            "reply": {
                "id": f"{branch}{i+1}",
                "title": options[i]
            }
        }
        buttons.append(button_)
    
    buttton = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": text
                },
                "footer": {
                    "text": footer
                },
                "action": {
                    "buttons": buttons
                }
            }
        }
    return buttton