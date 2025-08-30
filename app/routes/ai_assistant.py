from flask import Blueprint, request, jsonify
from app.services.ai_assistant import AIAssistant
from app.models import CodeSnippet, db

ai_bp = Blueprint('ai_assistant', __name__)

@ai_bp.route('/chat', methods=['POST'])
def chat():
    """AI-powered chat assistance"""
    try:
        data = request.get_json()
        message = data.get('message', '')
        context = data.get('context', {})
        
        ai_assistant = AIAssistant()
        response = ai_assistant.chat(message, context)
        
        return jsonify({
            'success': True,
            'response': response
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@ai_bp.route('/fix-error', methods=['POST'])
def fix_error():
    """AI-powered error fixing"""
    try:
        data = request.get_json()
        error_message = data.get('error_message', '')
        code = data.get('code', '')
        language = data.get('language', 'python')
        
        ai_assistant = AIAssistant()
        fixed_code = ai_assistant.fix_error(error_message, code, language)
        
        return jsonify({
            'success': True,
            'fixed_code': fixed_code
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@ai_bp.route('/code-snippets', methods=['GET'])
def get_code_snippets():
    """Get saved code snippets"""
    language = request.args.get('language')
    integration_type = request.args.get('type')
    
    query = CodeSnippet.query
    if language:
        query = query.filter_by(language=language)
    if integration_type:
        query = query.filter_by(integration_type=integration_type)
    
    snippets = query.all()
    return jsonify([snippet.to_dict() for snippet in snippets])

@ai_bp.route('/code-snippets', methods=['POST'])
def save_code_snippet():
    """Save a code snippet"""
    try:
        data = request.get_json()
        
        snippet = CodeSnippet(
            language=data['language'],
            integration_type=data['integration_type'],
            code=data['code'],
            description=data.get('description')
        )
        
        db.session.add(snippet)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'id': snippet.id
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500 