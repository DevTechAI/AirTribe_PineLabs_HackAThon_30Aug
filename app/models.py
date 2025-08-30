from datetime import datetime
from app import db

class Integration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    merchant_id = db.Column(db.String(100), nullable=False)
    integration_type = db.Column(db.String(50), nullable=False)  # 'payment', 'refund', 'status_check'
    status = db.Column(db.String(20), default='pending')  # 'pending', 'success', 'failed'
    request_payload = db.Column(db.Text, nullable=True)
    response_data = db.Column(db.Text, nullable=True)
    error_message = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'merchant_id': self.merchant_id,
            'integration_type': self.integration_type,
            'status': self.status,
            'request_payload': self.request_payload,
            'response_data': self.response_data,
            'error_message': self.error_message,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class CodeSnippet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(20), nullable=False)  # 'python', 'javascript', 'java', etc.
    integration_type = db.Column(db.String(50), nullable=False)
    code = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'language': self.language,
            'integration_type': self.integration_type,
            'code': self.code,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        } 