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
    # scheduler.add_job(func=lambda: ping_app(app), trigger="interval", minutes=2)
    scheduler.start()
    schedule_next_ping(app, scheduler)

def schedule_next_ping(app, scheduler):
    # Generate a random interval (e.g., between 1 and 5 minutes)

    random_minutes = random.randint(2, 4)
    next_run_time = datetime.now() + timedelta(minutes=random_minutes)

    # Schedule the ping_app function to run at next_run_time
    scheduler.add_job(func=lambda: ping_app(app, scheduler, random_minutes),trigger=DateTrigger(run_date=next_run_time))

def ping_app(app, scheduler, random_minutes):
    try:
        pid = os.getpid()
        url = DOMAIN.URL + '/health'
        response = requests.get(url)
        send_response(plain_txt(HOST.number, f'Pinged, Status Code: 200 / after {random_minutes} minutes {pid}'))
        schedule_next_ping(app, scheduler)
    except Exception as e:
        print(f'Error pinging the app: {e}')
        send_response(plain_txt(HOST.number, "Ping failed"))
        schedule_next_ping(app, scheduler)
        