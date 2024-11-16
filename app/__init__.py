from flask import Flask
from app.models.database.db import db
from app.config import Config
from app.stack.web.self_ping import start_scheduler

def create_app():
    app = Flask(__name__, template_folder = "./web/templates", static_folder = "./web/static")
    app.config.from_object(Config)
    
    db.init_app(app)

    with app.app_context():              
        from app.controllers import Routes
        Routes(app)
        
        db.create_all()
        
        start_scheduler(app) # scheduler for ping to the domain

    return app
