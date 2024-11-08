from app import db

class SchedulerStatus(db.Model):
    __tablename__ = 'scheduler_status'
    
    id = db.Column(db.Integer, primary_key=True)
    is_running = db.Column(db.Boolean, default=False)