from app.models.orm.customer import CustomerModel
from app import db

from datetime import datetime

class ClientRepository:
    @staticmethod
    def new(phone_number: str):
        """Stores client data into database.
        
        :param phone_number: String variable used to store in ClientModel the phone_number from which the inbound message originated.

        .. versionchanged:: 0.5
        """
        clientInstance = CustomerModel(phone_number=phone_number, status="new client", created_at=datetime.now())

        db.session.add(clientInstance)
        db.session.commit()
        