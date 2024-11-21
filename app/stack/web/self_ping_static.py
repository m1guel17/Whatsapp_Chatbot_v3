# new method to ping domain
from app.interfaces.generator.msg.json_format import plain_txt
from app.interfaces.api.whatsapp_api import send_response
from app.stack.constant.webdomain import DOMAIN
from app.stack.constant.host import HOST

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime, timedelta
import requests
import random
import os

def ping_scheduler(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=lambda: ping_app(app), trigger="interval", minutes=2)
    scheduler.start()

def ping_app(app):
    try:
        pid = os.getpid()
        url = DOMAIN.URL + '/health'
        response = requests.get(url)
        send_response(plain_txt(HOST.number, f'Pinged, Status Code: 200 / after 2 minutes {pid}'))
    except Exception as e:
        print(f'Error pinging the app: {e}')
        send_response(plain_txt(HOST.number, "Ping failed"))
        