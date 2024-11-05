from app.interfaces.crud.create.raw_repo import RawRepository as rawCreate
from app.interfaces.crud.read.raw_repo import RawRepository as rawRead

"""
    Services - Raw script to handle raw inbound message operations
    ----------------------------------------------------------------------------
    >Created: 2024-11-04
    >Last_modified: 2024-11-04
    >Author: Miguel
"""

class Raw:
    # ================================= CREATE =================================
    @staticmethod
    def registerRaw(inbound):
        rawCreate.new(inbound)
    
    # ================================== READ ==================================
    @staticmethod
    def get_all():
        return rawRead.get_all()

    # ================================= UPDATE =================================

        
    # ================================= DELETE =================================
    
    