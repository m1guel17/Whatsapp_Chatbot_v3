import os
# new class to ping domain
class DOMAIN:
    URL = os.environ.get('DOMAIN_URL', 'http://localhost:5000')