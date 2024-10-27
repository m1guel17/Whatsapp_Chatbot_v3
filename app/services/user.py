from app.core.crud.user_repository import UserRepository
from app.models.orm.user import UserModel

class User:

    @staticmethod
    def register(phone_number, name):
        user = UserModel(phone_number=phone_number, name=name)
        UserRepository.add_user(user)
        return user

    @staticmethod
    def findByPhone(phone_number):
        return UserRepository.get_user_by_phone(phone_number)
