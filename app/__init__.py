from flask import Flask
from app.models.database.db import db
from app.config import Config
#from app.stack.web.self_ping import ping_scheduler
from flask_apscheduler import APScheduler

scheduler = APScheduler()

def create_app():
    app = Flask(__name__, template_folder = "./web/templates", static_folder = "./web/static")
    app.config.from_object(Config)
    
    db.init_app(app)
    scheduler.init_app(app)
    scheduler.start()

    with app.app_context():              
        from app.controllers import Routes
        Routes(app)
        
        from app.core.jobs.inactive_check import check_inactive_users
        scheduler.add_job(id='InactivityChecker', func=check_inactive_users, trigger='interval', minutes=1)

        db.create_all()
        
        # ping_scheduler(app) # scheduler for ping to the domain

    return app
