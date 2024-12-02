from app.models.orm.message import MessagesModel
from app.models.orm.message import LastMessageModel
from app import db

from datetime import datetime
import json
import os

class MessageRepository:
    @staticmethod
    def by_phone(phone_number: str, content: str, status: str = None):
        """Updates LastMessageModel entries for the specified phone_number. The update occurs only if isRegistered is False; otherwise, the entries remain unchanged.
        
        :param phone_number: String variable used to update LastMessageModel with the phone_number from which the inbound message originated.
        :param content: String variable to update LastMessageModel with the inbound message.
        :param status: String/None variable to update MessagesModel based on the status of the conversation.
        
        .. versionchanged:: 2.1
        """
        sentAt = datetime.now()
        
        lastInstance = MessagesModel.query.filter_by(phone_number=phone_number).order_by(MessagesModel.id.desc()).first()
        lastNode = lastInstance.node
        lastChat = lastInstance.chat
        
        
        current_dir = os.path.dirname(__file__)
        json_path = os.path.join(current_dir, '..', '..', '..', 'core', 'json', 'chatflowv1.json')
        json_path = os.path.normpath(json_path)
        with open(json_path, 'r', encoding='utf-8') as f:
            CHATFLOW = json.load(f)
            
            
        nextNode = CHATFLOW["nodes"].get(lastNode)["next"]["default"]
        
        MessageInstance = MessagesModel(phone_number=phone_number, content=content, sent_at=sentAt, chat=lastChat+1, node = nextNode)
        
        lastMessageInstance = LastMessageModel.query.filter_by(phone_number=phone_number).first()
        lastMessageInstance.content = content
        lastMessageInstance.sent_at = sentAt
        
        if status:
            lastMessageInstance.status = status
        else:
            lastMessageInstance.status = "message received"
            
        db.session.add_all([MessageInstance, lastMessageInstance])
        db.session.commit()
    
    @staticmethod
    def by_phone2(phone_number: str, content: str, nodetype: str, nextNode: str):
        """Updates LastMessageModel entries for the specified phone_number. The update occurs only if isRegistered is False; otherwise, the entries remain unchanged.
        
        :param phone_number: String variable used to update LastMessageModel with the phone_number from which the inbound message originated.
        
        .. versionchanged:: 1.0
        """
        sentAt = datetime.now()
        
        lastInstance = MessagesModel.query.filter_by(phone_number=phone_number).order_by(MessagesModel.id.desc()).first()
        lastNode = lastInstance.node
        lastChat = lastInstance.chat
        
        MessageInstance = MessagesModel(phone_number=phone_number, content=content, sent_at=sentAt, chat=lastChat+1, node = nextNode, message_type=nodetype)
        
        lastMessageInstance = LastMessageModel.query.filter_by(phone_number=phone_number).first()
        lastMessageInstance.content = content
        lastMessageInstance.sent_at = sentAt
        
        db.session.add_all([MessageInstance, lastMessageInstance])
        db.session.commit()
    
    @staticmethod
    def by_phoneDynamic(phone_number: str, **kwargs):
        """Updates LastMessageModel entries for the specified phone_number. The update occurs only if isRegistered is False; otherwise, the entries remain unchanged.
        
        :param phone_number: String variable used to update LastMessageModel with the phone_number from which the inbound message originated.
        :param content: String variable to update LastMessageModel with the inbound message.
        :param status: String/None variable to update MessagesModel based on the status of the conversation.
        
        .. versionchanged:: 1.0
        """
        sentAt = datetime.now()
        
        lastInstance = MessagesModel.query.filter_by(phone_number=phone_number).order_by(MessagesModel.id.desc()).first()
        # lastNode = lastInstance.node
        lastChat = lastInstance.chat
        
        # customerInstance = MessagesModel.query.filter_by(phone_number=phone_number).first()
        customerInstance = MessagesModel(phone_number=phone_number, chat=lastChat+1, sent_at=sentAt)
        
        if customerInstance is not None:
            for key, value in kwargs.items():
                setattr(customerInstance, key, value)
            
            db.session.add(customerInstance)
            db.session.commit()
    
    
    @staticmethod
    def in_and_out_msg(phone_number: str, status: str):
        """Updates LastMessageModel entries for the specified phone_number. The update occurs only if isRegistered is False; otherwise, the entries remain unchanged.
        
        :param phone_number: String variable used to update LastMessageModel with the phone_number from which the inbound message originated.
        :param content: String variable to update LastMessageModel with the inbound message.
        
        .. versionchanged:: 0.2
        """
        sentAt = datetime.now()
        
        lastMessageInstance = LastMessageModel.query.filter_by(phone_number=phone_number).first()
        lastMessageInstance.sent_at = sentAt
        lastMessageInstance.status = status
        
        db.session.add(lastMessageInstance)
        db.session.commit()