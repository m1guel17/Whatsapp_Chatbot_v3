from app.models.orm.client import ClientModel
from app.models.database.db import db

class ClientRepository:
    @staticmethod
    def add(phone_number: str, isNew: bool):
        """Stores client data into database.
        
        :param phone_number: String variable used to store in ClientModel the phone_number from which the inbound message originated.
        :param isNew: Boolean variable to discern whether the client instance should be assigned 'potential client' status.

        .. versionchanged:: 0.1
        """
        if isNew:
            clientInstance = ClientModel(phone_number=phone_number, status="potential client")
            db.session.add(clientInstance)
            db.session.commit()
        