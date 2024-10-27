import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "KEYSSS"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///chatbot_demo.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class WHATSAPP_API:
    TOKEN = "Bearer " + os.environ.get('WHATSAPP_TOKEN')
    URL = 'graph.facebook.com'
    NUMBER_ID = os.environ.get('NUMBER_ID') 
    VERSION = os.environ.get('VERSION')
    REQUEST = VERSION + NUMBER_ID + '/messages'
    VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN') 
