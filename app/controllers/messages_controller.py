from flask import render_template, request, redirect, url_for
from app.services.message import Message
from app.services.client import Client
from app.services.user import User
#from app.models.database.db import db
from app import db

def messagesRoutes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        messages = Message.get_all()
        lasts = Message.fetch_last_msgs()
        clients = Client.get_all()
            
        return render_template('all_messages.html', registros=messages, lasts=lasts, clients=clients)
        #return render_template('all_messages.html', clients=clients)
    
    @app.route('/tables', methods=['GET', 'POST'])
    def tables():
        tables_info = {}
        for table_name, table in db.metadata.tables.items():
            columns = [{
                "name": column.name,
                "type": str(column.type),
                "nullable": column.nullable,
                "primary_key": column.primary_key
            } for column in table.columns]
            tables_info[table_name] = columns
            
        return render_template('all_tables.html', tables_info=tables_info)

    