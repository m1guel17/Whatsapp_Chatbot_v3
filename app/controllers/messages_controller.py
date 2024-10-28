from flask import render_template, request, redirect, url_for
from app.services.message import Message
from app.services.client import Client

def messagesRoutes(app):
    @app.route('/allMessages', methods=['GET', 'POST'])
    def index():
        messages = Message.get_all()
        lasts = Message.fetch_last_msgs()
        clients = Client.get_all()
        return render_template('all_messages.html', registros=messages, lasts=lasts, clients=clients)
