from app.interfaces.generator.msg.json_format import plain_txt
from app.interfaces.api.whatsapp_api import send_response
from app.models.orm.client import ClientModel
from app import db

from datetime import datetime, timedelta
from flask import current_app

def check_inactive_users():
    with current_app.app_context():
        now = datetime.now()
        timeout = now - timedelta(minutes=3)
        inactive_clients = ClientModel.query.filter(ClientModel.last_interaction < timeout).all()

        for client in inactive_clients:
            send_response(plain_txt(client.phone_number, "INACTIVE"))
            client.last_interaction = datetime.now()
            db.session.commit()
