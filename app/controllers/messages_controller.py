from flask import render_template, request, redirect, url_for
from app.services.message import Message

def messagesRoutes(app):
    @app.route('/allMessages', methods=['GET', 'POST'])
    def index():
        messages = Message.get_all()
        last = Message.get_last()
        return render_template('index.html', registros=messages, last = last)
