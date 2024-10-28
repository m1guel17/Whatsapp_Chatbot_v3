from flask import Flask
from app.models.database.db import db
from app.config import Config

def create_app():
    app = Flask(__name__, template_folder = "./web/templates", static_folder = "./web/static")
    app.config.from_object(Config)
    
    db.init_app(app)

    with app.app_context():
        from app.models.orm.message import MessagesModel, LastMessageModel
        from app.models.orm.user import UserModel
        from app.models.orm.client import ClientModel
                
        #from app.controllers import Routes
        #Routes(app)
        from app.controllers.chatbot_controller import chatbotRoutes
        from app.controllers.messages_controller import messagesRoutes
        chatbotRoutes(app)
        messagesRoutes(app)
        db.create_all()

    return app
