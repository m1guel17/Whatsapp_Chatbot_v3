from app.interfaces.generator.msg.json_format import plain_txt
from app.interfaces.api.whatsapp_api import send_response
from app.models.orm.client import ClientModel
from app import db

from datetime import datetime, timedelta
from flask import current_app

def check_inactive_users():
    now = datetime.now()
    timeout = now - timedelta(minutes=3)
    inactive_users = ClientModel.query.filter(ClientModel.last_interaction < timeout).all()

    for user in inactive_users:
        # Perform your desired action, e.g., send a reminder message
        send_response(plain_txt(user.phone_number, "INACTIVE"))
        
        # Update the last_interaction to prevent multiple messages
        user.last_interaction = datetime.now()
        db.session.commit()
