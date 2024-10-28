from app.models.orm.client import ClientModel
from app.models.database.db import db

from datetime import datetime

class ClientRepository:
    @staticmethod
    def add_client(phone_number: str, isNew: bool):
        """Stores client data into database.
        
        :param phone_number: String variable used to store in ClientModel the phone_number from which the inbound message originated.
        :param isNew: Boolean variable to discern whether the client instance should be assigned 'potential client' status.

        .. versionchanged:: 0.2
        """
        #if isNew:
        clientInstance = ClientModel(name="nice",phone_number=phone_number, status="potential client", created_at=datetime.utcnow(), lastOrder_id=1231233, lastOrder_on=datetime.utcnow())
        db.session.add(clientInstance)
        db.session.commit()
        