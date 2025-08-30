from flask import Blueprint, render_template, request, jsonify
from app.services.pine_labs import PineLabsService
from app.services.react_agent import ReActAgent
from app.models import Integration, db
import json

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@main_bp.route('/playground')
def playground():
    """Interactive API playground"""
    return render_template('playground.html')

@main_bp.route('/docs')
def docs():
    """Smart documentation page"""
    return render_template('docs.html')

@main_bp.route('/react')
def react_page():
    """ReAct Agent Interface"""
    return render_template('react_interface.html')

@main_bp.route('/test-integration', methods=['POST'])
def test_integration():
    """Test Pine Labs API integration"""
    try:
        data = request.get_json()
        
        # Create integration record
        integration = Integration(
            merchant_id=data.get('merchant_id', 'test_merchant'),
            integration_type=data.get('type', 'payment'),
            request_payload=json.dumps(data)
        )
        db.session.add(integration)
        db.session.commit()
        
        # Test the integration
        pine_service = PineLabsService()
        result = pine_service.test_integration(data)
        
        # Update integration record
        integration.status = 'success' if result.get('success') else 'failed'
        integration.response_data = json.dumps(result)
        if not result.get('success'):
            integration.error_message = result.get('error', 'Unknown error')
        db.session.commit()
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@main_bp.route('/generate-code', methods=['POST'])
def generate_code():
    """Generate code snippets for integration"""
    try:
        data = request.get_json()
        language = data.get('language', 'python')
        integration_type = data.get('type', 'payment')
        
        agent = ReActAgent()
        result = agent.reason_and_act(
            f"Generate {language} code for {integration_type} integration",
            {"action": "generate_code", "language": language, "integration_type": integration_type}
        )
        
        return jsonify({
            'success': True,
            'code': result.get('result', {}).get('code', ''),
            'language': language,
            'integration_type': integration_type
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500 