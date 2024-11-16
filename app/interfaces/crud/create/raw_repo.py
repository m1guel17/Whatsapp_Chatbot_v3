from app.models.orm.rawMsgs import RawModel
from app import db

from datetime import datetime
import json

class RawRepository:
    @staticmethod
    def new(inbound):
        """Stores json into database.
        
        :param inbound: variable used to store in RawModel the phone_number from which the inbound message originated.

        .. versionchanged:: 0.1
        """
        sentAt = datetime.utcnow()
        
        rawInstance = RawModel(content=json.dumps(inbound), sent_at=sentAt)
        
        db.session.add(rawInstance)
        db.session.commit()
        