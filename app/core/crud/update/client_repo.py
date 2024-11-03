from app.models.orm.databases import ClientModel
from app import db

from datetime import datetime

class ClientRepository:
    @staticmethod
    def by_phone(phone_number: str, **kwargs):
        """Updates ClientModel entry for the specified phone_number.
        
        :param phone_number: String variable used to update ClientModel instance
        :param **kwargs: Fields to update on the ClientModel instance
        
        .. versionchanged:: 0.1
        """
        clientInstance = ClientModel.query.filter_by(phone_number=phone_number).first()
        
        if clientInstance is not None:
            if 'lastOrder_id' in kwargs:
                kwargs['lastOrder_on'] = datetime.utcnow()
            
            for key, value in kwargs.items():
                setattr(clientInstance, key, value)
        
            db.session.commit()