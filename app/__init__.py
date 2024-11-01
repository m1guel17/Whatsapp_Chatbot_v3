from flask import Flask
from app.models.database.db import db
from app.config import Config

def create_app():
    app = Flask(__name__, template_folder = "./web/templates", static_folder = "./web/static")
    app.config.from_object(Config)
    
    db.init_app(app)

    with app.app_context():              
        from app.controllers import Routes
        Routes(app)
        
        db.create_all()

    return app
