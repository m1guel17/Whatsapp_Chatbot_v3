from app.services import Message
from app.services import Client
from app.interfaces.generator.msg.jsondump import msg
from app.interfaces.api.whatsapp_api import send_response

def saveText(phone_number: str, content: str):
    if Client.isNew(phone_number):
        Message.registerMsgs(phone_number, content)
        Client.registerClient(phone_number)
        send_response(msg(phone_number, "Bienvenido a Lian Accesorios ☺️, Enviamos captura pantalla de los productos que viste en live y quieres adquirir. El monto mínimo para separar tus productos es de 30 soles !!"))
        
    else:
        clientInstance = Client.get_one(phone_number)
        Message.update_by_phone(phone_number, content)

    
        if "status" in content:
            send_response(msg(phone_number, "status changed"))
            Client.update_status(phone_number, "client")
            
        
        elif "id" in content:
            send_response(msg(phone_number, "id generated"))
            Client.update_lastOrder_id(phone_number, 12089)