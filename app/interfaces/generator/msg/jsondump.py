
def msg(phone_number, message):
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