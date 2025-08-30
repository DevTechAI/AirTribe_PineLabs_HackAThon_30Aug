import json
import re
from typing import Dict, Any

def format_json(data: Any) -> str:
    """Format data as pretty JSON string"""
    try:
        return json.dumps(data, indent=2, sort_keys=True)
    except:
        return str(data)

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_amount(amount: Any) -> bool:
    """Validate amount is a positive number"""
    try:
        num = float(amount)
        return num > 0
    except (ValueError, TypeError):
        return False

def sanitize_string(text: str, max_length: int = 255) -> str:
    """Sanitize string input"""
    if not text:
        return ""
    
    # Remove potentially harmful characters
    sanitized = re.sub(r'[<>]', '', text)
    return sanitized[:max_length]

def generate_unique_id(prefix: str = "id") -> str:
    """Generate a unique ID with prefix"""
    import uuid
    return f"{prefix}_{str(uuid.uuid4())[:8]}"

def mask_sensitive_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Mask sensitive data in dictionary"""
    sensitive_keys = ['secret', 'key', 'token', 'password', 'api_key']
    masked_data = {}
    
    for key, value in data.items():
        if any(sensitive in key.lower() for sensitive in sensitive_keys):
            masked_data[key] = "***MASKED***"
        elif isinstance(value, dict):
            masked_data[key] = mask_sensitive_data(value)
        else:
            masked_data[key] = value
    
    return masked_data

def extract_error_details(error_response: Dict[str, Any]) -> Dict[str, Any]:
    """Extract meaningful error details from API response"""
    error_details = {
        'message': error_response.get('message', 'Unknown error'),
        'code': error_response.get('error_code', 'UNKNOWN'),
        'details': error_response.get('details', {}),
        'suggestions': []
    }
    
    # Add common suggestions based on error codes
    error_code = error_details['code'].lower()
    
    if 'auth' in error_code or 'credential' in error_code:
        error_details['suggestions'].append("Check your API credentials")
        error_details['suggestions'].append("Verify your merchant ID and secret key")
    
    elif 'amount' in error_code:
        error_details['suggestions'].append("Ensure amount is in paisa (multiply rupees by 100)")
        error_details['suggestions'].append("Check amount format (should be string)")
    
    elif 'timeout' in error_code:
        error_details['suggestions'].append("Check your internet connection")
        error_details['suggestions'].append("Implement retry logic for timeout errors")
    
    elif 'payload' in error_code or 'json' in error_code:
        error_details['suggestions'].append("Validate JSON structure")
        error_details['suggestions'].append("Check required fields are present")
    
    return error_details 