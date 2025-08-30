import requests
import json
import os
from typing import Dict, Any
import hashlib
import hmac
import base64

class PineLabsService:
    def __init__(self):
        self.base_url = os.getenv('PINE_LABS_BASE_URL', 'https://api-sandbox.pinelabs.com')
        self.merchant_id = os.getenv('PINE_LABS_MERCHANT_ID')
        self.secret_key = os.getenv('PINE_LABS_SECRET_KEY')
    
    def validate_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Validate API payload structure and required fields"""
        errors = []
        
        # Common validation rules for different integration types
        if payload.get('type') == 'payment':
            required_fields = ['amount', 'currency', 'merchant_order_id']
            for field in required_fields:
                if field not in payload:
                    errors.append(f"Missing required field: {field}")
            
            # Validate amount
            if 'amount' in payload:
                try:
                    amount = float(payload['amount'])
                    if amount <= 0:
                        errors.append("Amount must be greater than 0")
                except (ValueError, TypeError):
                    errors.append("Invalid amount format")
        
        elif payload.get('type') == 'refund':
            required_fields = ['original_transaction_id', 'refund_amount']
            for field in required_fields:
                if field not in payload:
                    errors.append(f"Missing required field: {field}")
        
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'suggestions': self._get_suggestions(payload.get('type'), errors)
        }
    
    def _get_suggestions(self, integration_type: str, errors: list) -> list:
        """Get suggestions to fix validation errors"""
        suggestions = []
        
        if integration_type == 'payment':
            if any('amount' in error for error in errors):
                suggestions.append("Amount should be in paisa (e.g., 100.00 for ₹1.00)")
            if any('merchant_order_id' in error for error in errors):
                suggestions.append("Use a unique order ID for each transaction")
        
        return suggestions
    
    def test_integration(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Test integration with Pine Labs API"""
        try:
            # Validate payload first
            validation = self.validate_payload(payload)
            if not validation['valid']:
                return {
                    'success': False,
                    'error': 'Validation failed',
                    'validation_errors': validation['errors'],
                    'suggestions': validation['suggestions']
                }
            
            # For demo purposes, simulate API call
            # In production, this would make actual HTTP request
            if payload.get('type') == 'payment':
                return self._simulate_payment(payload)
            elif payload.get('type') == 'refund':
                return self._simulate_refund(payload)
            else:
                return self._simulate_status_check(payload)
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _simulate_payment(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate payment API response"""
        # Simulate different scenarios based on payload
        if payload.get('amount', 0) > 50000:  # Simulate high amount rejection
            return {
                'success': False,
                'error': 'Amount exceeds daily limit',
                'error_code': 'AMOUNT_LIMIT_EXCEEDED'
            }
        
        return {
            'success': True,
            'transaction_id': f'txn_{hash(str(payload)) % 1000000}',
            'status': 'success',
            'amount': payload.get('amount'),
            'currency': payload.get('currency', 'INR'),
            'merchant_order_id': payload.get('merchant_order_id')
        }
    
    def _simulate_refund(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate refund API response"""
        return {
            'success': True,
            'refund_id': f'refund_{hash(str(payload)) % 1000000}',
            'status': 'processed',
            'amount': payload.get('refund_amount'),
            'original_transaction_id': payload.get('original_transaction_id')
        }
    
    def _simulate_status_check(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate status check API response"""
        return {
            'success': True,
            'transaction_id': payload.get('transaction_id'),
            'status': 'completed',
            'amount': 1000.00,
            'timestamp': '2024-01-01T10:00:00Z'
        }
    
    def simulate_response(self, scenario: str) -> Dict[str, Any]:
        """Simulate different API response scenarios for testing"""
        scenarios = {
            'success': {
                'success': True,
                'transaction_id': 'txn_123456',
                'status': 'completed',
                'amount': 1000.00
            },
            'failure': {
                'success': False,
                'error': 'Invalid credentials',
                'error_code': 'AUTH_FAILED'
            },
            'timeout': {
                'success': False,
                'error': 'Request timeout',
                'error_code': 'TIMEOUT'
            },
            'invalid_payload': {
                'success': False,
                'error': 'Invalid JSON payload',
                'error_code': 'INVALID_PAYLOAD'
            }
        }
        
        return scenarios.get(scenario, scenarios['success'])
    
    def generate_signature(self, payload: Dict[str, Any]) -> str:
        """Generate HMAC signature for API requests"""
        # Sort payload keys
        sorted_payload = json.dumps(payload, sort_keys=True)
        
        # Create HMAC signature
        signature = hmac.new(
            self.secret_key.encode(),
            sorted_payload.encode(),
            hashlib.sha256
        ).hexdigest()
        
        return signature 