from app.controllers.chatbot_controller import chatbotRoutes
from app.controllers.tables_controller import tablesRoutes


def Routes(app):
    chatbotRoutes(app)
    tablesRoutes(app)
