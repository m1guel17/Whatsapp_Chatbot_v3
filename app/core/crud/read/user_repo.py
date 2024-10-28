from app.models.orm.user import UserModel
from app.models.database.db import db

from werkzeug.security import  check_password_hash

class UserRepository:
    @staticmethod
    def get_by_phone(phone_number: str):
        """Returns UserModel instance filterd by phone_number.

        :param phone_number: String variable to select one row from UserModel.
        
        .. versionchanged:: 0.1
        """
        return UserModel.query.filter_by(phone_number=phone_number).first()
    
    @staticmethod
    def check_password(userModelRow, password: str) -> bool:
        """Checks that the given password matches the one stored in db that was previously generated when the user first registered or update their password. Returns boolean value.

        :param userModelRow: Instance from database filtered by username or phone_number.
        :param password: String variable, is the plaintext password from web.

        .. versionchanged:: 0.1
        """
        return check_password_hash(userModelRow.password_hash, password)
    