from flask import Blueprint, request, jsonify
from app.services.pine_labs import PineLabsService
from app.models import Integration, db
import json

api_bp = Blueprint('api', __name__)

@api_bp.route('/integrations', methods=['GET'])
def get_integrations():
    """Get all integration attempts"""
    merchant_id = request.args.get('merchant_id')
    
    query = Integration.query
    if merchant_id:
        query = query.filter_by(merchant_id=merchant_id)
    
    integrations = query.order_by(Integration.created_at.desc()).all()
    return jsonify([integration.to_dict() for integration in integrations])

@api_bp.route('/integrations/<int:integration_id>', methods=['GET'])
def get_integration(integration_id):
    """Get specific integration details"""
    integration = Integration.query.get_or_404(integration_id)
    return jsonify(integration.to_dict())

@api_bp.route('/validate-payload', methods=['POST'])
def validate_payload():
    """Validate API payload structure"""
    try:
        data = request.get_json()
        pine_service = PineLabsService()
        
        validation_result = pine_service.validate_payload(data)
        return jsonify(validation_result)
        
    except Exception as e:
        return jsonify({
            'valid': False,
            'errors': [str(e)]
        }), 500

@api_bp.route('/simulate-response', methods=['POST'])
def simulate_response():
    """Simulate API responses for testing"""
    try:
        data = request.get_json()
        scenario = data.get('scenario', 'success')
        
        pine_service = PineLabsService()
        simulated_response = pine_service.simulate_response(scenario)
        
        return jsonify(simulated_response)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500 