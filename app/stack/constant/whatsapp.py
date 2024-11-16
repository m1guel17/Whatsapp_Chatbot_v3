import os

class WHATSAPP_API:
    TOKEN = "Bearer " + os.environ.get('WHATSAPP_TOKEN')
    URL = 'graph.facebook.com'
    NUMBER_ID = os.environ.get('NUMBER_ID') 
    VERSION = os.environ.get('VERSION')
    REQUEST = VERSION + NUMBER_ID + '/messages'
    VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN') 
