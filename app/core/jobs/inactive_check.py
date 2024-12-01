from app.interfaces.generator.msg.json_format import plain_txt
from app.interfaces.api.whatsapp_api import send_response
from app.models.orm.client import CustomersModel
from app import db

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

def inactivity_schedule(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=lambda: check_inactive_users(app), trigger="interval", minutes=2)
    scheduler.start()
    
def check_inactive_users(app):
    with app.app_context():
        now = datetime.now() #
        wait_threshold = datetime.now() - timedelta(minutes=2)
        inactive_clients = CustomersModel.query.filter(CustomersModel.last_interaction <= wait_threshold,  CustomersModel.status != "chat inactive").all()

        for client in inactive_clients:
            refresh = CustomersModel.query.filter(CustomersModel.last_interaction == client.phone_number).order_by(CustomersModel.id.desc()).first() #
            if refresh.last_interaction > wait_threshold: #
                continue #
            
            send_response(plain_txt(client.phone_number, "INACTIVE"))
            client.last_interaction = datetime.now()
            client.status = "chat inactive"
            db.session.commit()
