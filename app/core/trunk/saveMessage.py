from app.services.message import Message

def saveText(content, phone_number):
    Message.register(phone_number, content)