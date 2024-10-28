from app.models.orm.client import ClientModel
from app.models.database.db import db

class ClientRepository:
    @staticmethod
    def check_if_isNew(phone_number: str) -> bool:
        """Gets the first instace from a phone_number in ClientModel.
        
        :param phone_number: String variable used to check in ClientModel if the client with phone_number is registered.
        
        .. versionchanged:: 0.1
        """
        return ClientModel.query.filter_by(phone_number=phone_number).first() is None
