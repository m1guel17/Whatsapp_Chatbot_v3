from app.models.database.db import db

from werkzeug.security import generate_password_hash

class UserRepository:
    @staticmethod
    def add(user):
        """Stores user data into database.
        
        :param user: UserModel instace.

        .. versionchanged:: 0.1
        """
        db.session.add(user)
        db.session.commit()
    
    @staticmethod
    def set_password(password: str) -> str:
        """Securely hash a password for storage.
        
        :param password: String variable, is the plaintext password from web.

        .. versionchanged:: 0.1
        """
        return generate_password_hash(password)
    