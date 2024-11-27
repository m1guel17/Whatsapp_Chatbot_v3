from flask import render_template, request, redirect, url_for
from app.models.orm import *
from app.services import Client, Message, Raw
from app import db

def tablesRoutes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        clients = Client.get_all()
        messages = Message.get_all()
        lasts = Message.fetch_last_msgs()
            
        return render_template('all_messages.html', registros=messages, lasts=lasts, clients=clients)
    
    @app.route('/raw')
    def raw():
        raws = Raw.get_all()
            
        return render_template('raw.html', raws=raws)
    
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

    