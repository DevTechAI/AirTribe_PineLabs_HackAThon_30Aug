from flask import Blueprint, request, jsonify, render_template
from app.services.react_agent import ReActAgent
import json

react_bp = Blueprint('react_assistant', __name__)

# Global agent instance
react_agent = ReActAgent()

@react_bp.route('/')
def react_interface():
    """ReAct Agent Interface"""
    return render_template('react_interface.html')

@react_bp.route('/chat', methods=['POST'])
def chat():
    """Handle ReAct agent conversation"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        context = data.get('context', {})
        
        if not user_message:
            return jsonify({
                'success': False,
                'error': 'Message is required'
            }), 400
        
        # Process through ReAct agent
        response = react_agent.reason_and_act(user_message, context)
        
        return jsonify({
            'success': True,
            'response': response.get('response', ''),
            'reasoning': response.get('reasoning', ''),
            'action_taken': response.get('action_taken'),
            'observation': response.get('observation', ''),
            'result': response.get('result', {}),
            'timestamp': json.dumps(response.get('timestamp', ''))
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@react_bp.route('/conversation', methods=['GET'])
def get_conversation():
    """Get conversation history"""
    try:
        history = react_agent.get_conversation_history()
        return jsonify({
            'success': True,
            'conversation': history
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@react_bp.route('/clear', methods=['POST'])
def clear_conversation():
    """Clear conversation history"""
    try:
        react_agent.clear_conversation()
        return jsonify({
            'success': True,
            'message': 'Conversation cleared'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@react_bp.route('/actions', methods=['GET'])
def get_available_actions():
    """Get list of available actions"""
    actions = {
        'generate_code': {
            'description': 'Generate integration code in Python, JavaScript, or Java',
            'parameters': {
                'language': 'Programming language (python, javascript, java)',
                'integration_type': 'Type of integration (payment, refund, status_check)'
            }
        },
        'validate_payload': {
            'description': 'Validate API payload structure and required fields',
            'parameters': {
                'payload': 'API payload object to validate'
            }
        },
        'test_integration': {
            'description': 'Test Pine Labs API integration with provided payload',
            'parameters': {
                'payload': 'API payload to test',
                'merchant_id': 'Merchant ID for testing'
            }
        },
        'fix_error': {
            'description': 'Fix integration errors and provide corrected code',
            'parameters': {
                'error_message': 'Error message to fix',
                'code': 'Current code that has errors',
                'language': 'Programming language'
            }
        }
    }
    
    return jsonify({
        'success': True,
        'actions': actions
    }) 