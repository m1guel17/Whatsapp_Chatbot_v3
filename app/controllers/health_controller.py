# new method to ping domain
def health_check_(app):
    @app.route('/health', methods=['GET'])
    def health_check():
        return 'OK', 200