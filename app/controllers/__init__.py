from app.controllers.chatbot_controller import chatbotRoutes
from app.controllers.tables_controller import tablesRoutes
from app.controllers.health_controller import health_check_

def Routes(app):
    chatbotRoutes(app)
    tablesRoutes(app)
    health_check_(app)