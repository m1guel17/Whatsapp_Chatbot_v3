from app.models.database.db import db

class UserRepository:
    @staticmethod
    def add(user):
        db.session.add(user)
        db.session.commit()