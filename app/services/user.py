from app.core.crud.create.user_repo import UserRepository as userCreate
from app.core.crud.read.user_repo import UserRepository as userRead
from app.models.orm.user import UserModel

class User:
    @staticmethod
    def register(phone_number, name):
        user = UserModel(phone_number=phone_number, name=name)
        userCreate.add(user)

    @staticmethod
    def findByPhone(phone_number):
        return userRead.get_by_phone(phone_number)
