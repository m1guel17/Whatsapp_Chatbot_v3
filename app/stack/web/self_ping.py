# new method to ping domain
from app.interfaces.generator.msg.json_format import plain_txt
from app.interfaces.api.whatsapp_api import send_response
from app.stack.constant.webdomain import DOMAIN
from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
import requests
import random

def start_scheduler(app):
    scheduler = BackgroundScheduler()
    # scheduler.add_job(func=lambda: ping_app(app), trigger="interval", minutes=2)
    scheduler.start()
    schedule_next_ping(app, scheduler)

def schedule_next_ping(app, scheduler):
    # Generate a random interval (e.g., between 1 and 5 minutes)

    random_minutes = random.randint(1, 2)
    next_run_time = datetime.now() + timedelta(minutes=random_minutes)

    # Schedule the ping_app function to run at next_run_time
    scheduler.add_job(func=lambda: ping_app(app, scheduler, random_minutes),trigger=DateTrigger(run_date=next_run_time))

def ping_app(app, scheduler, random_minutes):
    try:
        url = DOMAIN.URL + '/health'
        send_response(plain_txt("51998249361", url))
        response = requests.get(url)
        #send_response(plain_txt("51998249361", response.text))
        #print(f'Pinged {url}, Status Code: {response.status_code}')
        send_response(plain_txt("51998249361", "Pinged, Status Code: 200 / after x minutes"))
        # After the ping, schedule the next ping
        schedule_next_ping(app, scheduler)
    except Exception as e:
        print(f'Error pinging the app: {e}')
        #send_response(plain_txt("51998249361", "Ping failed"))
        send_response(plain_txt("51998249361", "Ping failed"))
        schedule_next_ping(app, scheduler)
        