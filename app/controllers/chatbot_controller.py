from flask import request, jsonify
from app.core.robot.entryDealer import receive_message
from app.config import WHATSAPP_API

def chatbotRoutes(app):
    @app.route('/webhook', methods=['GET', 'POST'])
    def webhook():
        if request.method == 'GET':
                challenge = verify_token(request)
                return challenge
        elif request.method == 'POST':
            response = receive_message(request)
            return response
            
    def verify_token(req):
        token = req.args.get('hub.verify_token')
        challenge = req.args.get('hub.challenge')
        if challenge and token == WHATSAPP_API.VERIFY_TOKEN:
            return challenge
        else:
            return jsonify({'error': 'Token Invalido'}), 401


