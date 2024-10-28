from flask import render_template, request, redirect, url_for
from app.services.message import Message

def messagesRoutes(app):
    @app.route('/allMessages', methods=['GET', 'POST'])
    def index():
        messages = Message.get_all()
        lasts = Message.fetch_last_msgs()
        return render_template('all_messages.html', registros=messages, lasts=lasts)
