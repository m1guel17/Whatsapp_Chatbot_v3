from app.models.database.db import db

from werkzeug.security import generate_password_hash

class UserRepository:
    @staticmethod
    def add(user):
        db.session.add(user)
        db.session.commit()
    
    @staticmethod
    def set_password(password: str) -> str:
        """Returns a hashed password generated from string input.
        
        :param password: String variable, is the plaintext password from web.

        .. versionchanged:: 0.1
        """
        return generate_password_hash(password)
    