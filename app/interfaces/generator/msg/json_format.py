
def plain_txt(phone_number, message):
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

def button(number, text, footer, id, options):
    buttons = []
    for i in range(len(options)):
        button_ = {
            "type": "reply",
            "reply": {
                "id": id[i],
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