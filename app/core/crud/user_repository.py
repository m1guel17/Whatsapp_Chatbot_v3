from app.models.orm.user import UserModel
from app.models.database.db import db

class UserRepository:
    @staticmethod
    def get_user_by_phone(phone_number):
        return UserModel.query.filter_by(phone_number=phone_number).first()

    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()
