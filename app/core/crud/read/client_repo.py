from app.models.orm.databases import ClientModel
# from app.models.database.db import db
from app import db

class ClientRepository:
    @staticmethod
    def check_if_isNew(phone_number: str) -> bool:
        """Gets the first instace from a phone_number in ClientModel.
        
        :param phone_number: String variable used to check in ClientModel if the client with phone_number is registered.
        
        .. versionchanged:: 0.2
        """
        return ClientModel.query.filter_by(phone_number=phone_number).first() is None
        # row = ClientModel.query.filter_by(phone_number=phone_number).first()
        # if row is not None:
        #     return False
        # else:
        #     return True

    @staticmethod
    def get_all_clients():
        """Gets all the rows in ClientModel.
        
        .. versionchanged:: 0.1
        """
        return ClientModel.query.all()
    