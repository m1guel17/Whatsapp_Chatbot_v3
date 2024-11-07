# new method to ping domain
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from app.stack.constant.webdomain import DOMAIN

from app.interfaces.api.whatsapp_api import send_response
from app.interfaces.generator.msg.json_format import plain_txt

def start_scheduler(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=lambda: ping_app(app), trigger="interval", minutes=2)
    scheduler.start()

def ping_app(app):
    with app.app_context():
        try:
            url = DOMAIN.URL + '/health'
            response = requests.get(url)
            print(f'Pinged {url}, Status Code: {response.status_code}')
            send_response(plain_txt("51998249361", "Ping to server"))
        except Exception as e:
            print(f'Error pinging the app: {e}')
            send_response(plain_txt("51998249361", "Ping failed"))