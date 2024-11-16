from app.models.orm.rawMsgs import RawModel
from app import db


class RawRepository:
    @staticmethod
    def get_all():
        """Gets all the rows in RawModel.
        
        .. versionchanged:: 0.1
        """
        return RawModel.query.all()
        