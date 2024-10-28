from app.core.crud.create.user_repo import UserRepository as userCreate
from app.core.crud.read.user_repo import UserRepository as userRead
from app.models.orm.user import UserModel

"""
    Services - User script to handle users operations
    ----------------------------------------------------------------------------
    >Created: @2024-10-27
    >Last_modified: 2024-10-26
    >Author: Miguel
"""

class User:
    # ================================= CREATE =================================
    @staticmethod
    def register(phone_number: str, name: str, username: str, password: str, isAdmin: bool):
        password_hash = userCreate.set_password(password)
        user = UserModel(name=name, phone_number=phone_number, username=username, password_hash=password_hash, is_admin=isAdmin, status="active")
        userCreate.add(user)

    # ================================== READ ==================================
    @staticmethod
    def findByUsername(username: str):
        return userRead.get_by_username(username)
    
    @staticmethod
    def findByPhone(phone_number: str):
        return userRead.get_by_phone(phone_number)
    
    @staticmethod
    def authenticateUser(username: str, passwordFromWeb: str):
        return User.checkPassword4Login(User.findByUsername(username), passwordFromWeb)

    @staticmethod
    def checkPassword4Login(userModelRow, passwordFromWeb: str):
        return userRead.check_password(userModelRow, passwordFromWeb)
    
    # ================================= UPDATE =================================
    
    
    # ================================= DELETE =================================
    
    