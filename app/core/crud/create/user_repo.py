from app.models.database.db import db

from werkzeug.security import generate_password_hash

class UserRepository:
    @staticmethod
    def add(user):
        db.session.add(user)
        db.session.commit()
    
    @staticmethod
    def set_password(password):
        return generate_password_hash(password)
    