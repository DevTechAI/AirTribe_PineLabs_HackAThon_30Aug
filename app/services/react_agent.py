import openai
import os
import json
import re
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from app.services.pine_labs import PineLabsService
from app.models import Integration, db
import colorama
from colorama import Fore, Style

colorama.init()

class Action:
    """Represents an action the ReAct agent can take"""
    
    def __init__(self, name: str, description: str, parameters: Dict[str, Any] = None):
        self.name = name
        self.description = description
        self.parameters = parameters or {}
    
    def execute(self, **kwargs) -> Dict[str, Any]:
        """Execute the action with given parameters"""
        raise NotImplementedError("Subclasses must implement execute method")

class GenerateCodeAction(Action):
    """Action to generate integration code"""
    
    def __init__(self):
        super().__init__(
            "generate_code",
            "Generate integration code in a specific language for Pine Labs API",
            {
                "language": {"type": "string", "description": "Programming language (python, javascript, java)"},
                "integration_type": {"type": "string", "description": "Type of integration (payment, refund, status_check)"}
            }
        )
    
    def execute(self, language: str, integration_type: str) -> Dict[str, Any]:
        """Generate code using OpenAI"""
        try:
            prompts = {
                'python': {
                    'payment': """
                    Generate Python code for Pine Labs payment integration using requests library.
                    Include proper error handling, payload validation, and response parsing.
                    Use the sandbox environment. Make it production-ready.
                    """,
                    'refund': """
                    Generate Python code for Pine Labs refund API integration.
                    Include transaction ID validation and response handling.
                    """,
                    'status_check': """
                    Generate Python code to check transaction status with Pine Labs API.
                    Include proper polling mechanism and status interpretation.
                    """
                },
                'javascript': {
                    'payment': """
                    Generate JavaScript/Node.js code for Pine Labs payment integration using axios.
                    Include async/await, error handling, and response validation.
                    """,
                    'refund': """
                    Generate JavaScript code for Pine Labs refund API call.
                    """,
                    'status_check': """
                    Generate JavaScript code for transaction status checking.
                    """
                },
                'java': {
                    'payment': """
                    Generate Java code using HttpClient for Pine Labs payment integration.
                    Include proper JSON handling and exception management.
                    """,
                    'refund': """
                    Generate Java code for refund processing.
                    """,
                    'status_check': """
                    Generate Java code for status checking.
                    """
                }
            }
            
            prompt = prompts.get(language, {}).get(integration_type, 
                f"Generate {language} code for {integration_type} integration with Pine Labs API")
            
            messages = [
                {"role": "system", "content": "You are a code generation assistant specialized in payment API integrations."},
                {"role": "user", "content": prompt}
            ]
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=1000,
                temperature=0.3
            )
            
            code = response.choices[0].message.content.strip()
            
            return {
                "success": True,
                "code": code,
                "language": language,
                "integration_type": integration_type
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

class ValidatePayloadAction(Action):
    """Action to validate API payload"""
    
    def __init__(self):
        super().__init__(
            "validate_payload",
            "Validate Pine Labs API payload structure and required fields",
            {
                "payload": {"type": "object", "description": "API payload to validate"}
            }
        )
    
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Validate payload using PineLabsService"""
        pine_service = PineLabsService()
        validation_result = pine_service.validate_payload(payload)
        return validation_result

class TestIntegrationAction(Action):
    """Action to test Pine Labs integration"""
    
    def __init__(self):
        super().__init__(
            "test_integration",
            "Test Pine Labs API integration with provided payload",
            {
                "payload": {"type": "object", "description": "API payload to test"},
                "merchant_id": {"type": "string", "description": "Merchant ID for testing"}
            }
        )
    
    def execute(self, payload: Dict[str, Any], merchant_id: str = "test_merchant") -> Dict[str, Any]:
        """Test integration and store results"""
        try:
            # Create integration record
            integration = Integration(
                merchant_id=merchant_id,
                integration_type=payload.get('type', 'payment'),
                request_payload=json.dumps(payload)
            )
            db.session.add(integration)
            db.session.commit()
            
            # Test the integration
            pine_service = PineLabsService()
            result = pine_service.test_integration(payload)
            
            # Update integration record
            integration.status = 'success' if result.get('success') else 'failed'
            integration.response_data = json.dumps(result)
            if not result.get('success'):
                integration.error_message = result.get('error', 'Unknown error')
            db.session.commit()
            
            return result
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

class FixErrorAction(Action):
    """Action to fix integration errors"""
    
    def __init__(self):
        super().__init__(
            "fix_error",
            "Fix integration errors and provide corrected code",
            {
                "error_message": {"type": "string", "description": "Error message to fix"},
                "code": {"type": "string", "description": "Current code that has errors"},
                "language": {"type": "string", "description": "Programming language"}
            }
        )
    
    def execute(self, error_message: str, code: str, language: str) -> Dict[str, Any]:
        """Fix errors using AI"""
        try:
            prompt = f"""
            I have this {language} code that's causing an error with Pine Labs API integration:
            
            Error: {error_message}
            
            Code:
            {code}
            
            Please fix the error and provide the corrected code with explanations.
            Focus on Pine Labs API best practices and common integration mistakes.
            """
            
            messages = [
                {"role": "system", "content": "You are an expert in fixing payment API integration errors."},
                {"role": "user", "content": prompt}
            ]
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=1000,
                temperature=0.2
            )
            
            fixed_code = response.choices[0].message.content.strip()
            
            return {
                "success": True,
                "fixed_code": fixed_code,
                "language": language
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

class ReActAgent:
    """ReAct (Reasoning and Acting) Agent for Pine Labs Integration"""
    
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.model = "gpt-3.5-turbo"
        
        # Define available actions
        self.actions = {
            "generate_code": GenerateCodeAction(),
            "validate_payload": ValidatePayloadAction(),
            "test_integration": TestIntegrationAction(),
            "fix_error": FixErrorAction()
        }
        
        # Conversation history
        self.conversation_history = []
        
        # Current task state
        self.current_task = None
        self.task_progress = []
    
    def reason_and_act(self, user_input: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Main ReAct loop: Reason about user input and take appropriate action"""
        
        # Add user input to conversation
        self.conversation_history.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.now().isoformat()
        })
        
        # Step 1: REASON - Analyze the user input and decide what to do
        reasoning_result = self._reason(user_input, context)
        
        # Step 2: ACT - Execute the chosen action
        if reasoning_result.get("action_needed"):
            action_result = self._act(reasoning_result)
            
            # Step 3: OBSERVE - Analyze the action result
            observation = self._observe(action_result, reasoning_result)
            
            # Step 4: RESPOND - Generate final response
            response = self._respond(observation, reasoning_result)
        else:
            # No action needed, just respond
            response = {
                "success": True,
                "response": reasoning_result.get("response", "I understand. How can I help you with Pine Labs integration?"),
                "reasoning": reasoning_result.get("reasoning", ""),
                "action_taken": None
            }
        
        # Add agent response to conversation
        self.conversation_history.append({
            "role": "assistant",
            "content": response.get("response", ""),
            "timestamp": datetime.now().isoformat(),
            "reasoning": response.get("reasoning", ""),
            "action_taken": response.get("action_taken")
        })
        
        return response
    
    def _reason(self, user_input: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Reason about what action to take based on user input"""
        
        # Create reasoning prompt
        system_prompt = """
        You are a ReAct agent specialized in Pine Labs payment API integration.
        Your task is to analyze user requests and decide what actions to take.
        
        Available actions:
        1. generate_code: Generate integration code in Python, JavaScript, or Java
        2. validate_payload: Validate API payload structure and required fields
        3. test_integration: Test Pine Labs API integration with provided payload
        4. fix_error: Fix integration errors and provide corrected code
        
        For each user request, you should:
        1. Analyze what the user is asking for
        2. Determine if an action is needed
        3. If yes, specify which action and its parameters
        4. Provide reasoning for your decision
        
        Respond in this exact JSON format:
        {
            "reasoning": "Your step-by-step reasoning",
            "action_needed": true/false,
            "action": "action_name",
            "parameters": {"param1": "value1", "param2": "value2"},
            "response": "What you would say to the user if no action is needed"
        }
        """
        
        # Build context string
        context_str = ""
        if context:
            context_str = f"\nCurrent context: {json.dumps(context)}"
        
        if self.conversation_history:
            recent_history = self.conversation_history[-3:]  # Last 3 messages
            context_str += f"\nRecent conversation: {json.dumps(recent_history)}"
        
        user_prompt = f"""
        User request: {user_input}{context_str}
        
        Analyze this request and decide what action to take.
        """
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=800,
                temperature=0.3
            )
            
            # Parse JSON response
            result_text = response.choices[0].message.content.strip()
            
            # Try to extract JSON from response
            json_match = re.search(r'\{.*\}', result_text, re.DOTALL)
            if json_match:
                result_text = json_match.group()
            
            result = json.loads(result_text)
            return result
            
        except Exception as e:
            print(f"❌ Reasoning error: {str(e)}")
            return {
                "reasoning": f"Error in reasoning process: {str(e)}",
                "action_needed": False,
                "response": "I'm having trouble understanding your request. Could you please rephrase it?"
            }
    
    def _act(self, reasoning_result: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the chosen action"""
        
        action_name = reasoning_result.get("action")
        parameters = reasoning_result.get("parameters", {})
        
        if action_name not in self.actions:
            return {
                "success": False,
                "error": f"Unknown action: {action_name}",
                "action": action_name
            }
        
        action = self.actions[action_name]
        
        try:
            print(f"🔧 Executing action: {action_name}")
            result = action.execute(**parameters)
            print(f"✅ Action {action_name} completed")
            return {
                "success": True,
                "action": action_name,
                "result": result
            }
            
        except Exception as e:
            print(f"❌ Action {action_name} failed: {str(e)}")
            return {
                "success": False,
                "action": action_name,
                "error": str(e)
            }
    
    def _observe(self, action_result: Dict[str, Any], reasoning_result: Dict[str, Any]) -> Dict[str, Any]:
        """Observe and analyze the action result"""
        
        if not action_result.get("success"):
            return {
                "observation": f"Action failed: {action_result.get('error', 'Unknown error')}",
                "success": False,
                "needs_followup": True
            }
        
        action_name = action_result.get("action")
        result = action_result.get("result", {})
        
        # Analyze different action results
        if action_name == "generate_code":
            observation = f"Generated {result.get('language')} code for {result.get('integration_type')} integration"
            
        elif action_name == "validate_payload":
            if result.get("valid"):
                observation = "Payload validation successful - all required fields present"
            else:
                observation = f"Payload validation failed: {', '.join(result.get('errors', []))}"
                
        elif action_name == "test_integration":
            if result.get("success"):
                observation = f"Integration test successful - {result.get('transaction_id', 'N/A')}"
            else:
                observation = f"Integration test failed: {result.get('error', 'Unknown error')}"
                
        elif action_name == "fix_error":
            observation = "Error fixed and corrected code generated"
            
        else:
            observation = f"Action {action_name} completed successfully"
        
        return {
            "observation": observation,
            "success": action_result.get("success"),
            "result": result,
            "needs_followup": False
        }
    
    def _respond(self, observation: Dict[str, Any], reasoning_result: Dict[str, Any]) -> Dict[str, Any]:
        """Generate final response to user"""
        
        success = observation.get("success", False)
        action_name = reasoning_result.get("action")
        
        if success:
            # Create response based on action result
            if action_name == "generate_code":
                response_text = "I've generated the integration code for you! Here's what I created:"
                
            elif action_name == "validate_payload":
                if observation.get("result", {}).get("valid"):
                    response_text = "✅ Your payload is valid! Ready to test the integration."
                else:
                    response_text = "⚠️ I found some issues with your payload. Let me help you fix them."
                    
            elif action_name == "test_integration":
                if observation.get("result", {}).get("success"):
                    response_text = "🎉 Integration test successful! Your setup is working correctly."
                else:
                    response_text = "❌ Integration test failed. Let me help you troubleshoot this."
                    
            elif action_name == "fix_error":
                response_text = "🔧 I've fixed the error in your code. Here's the corrected version:"
                
            else:
                response_text = "✅ Task completed successfully!"
                
        else:
            response_text = f"❌ I encountered an issue: {observation.get('observation', 'Unknown error')}"
        
        return {
            "success": success,
            "response": response_text,
            "reasoning": reasoning_result.get("reasoning", ""),
            "action_taken": action_name,
            "observation": observation.get("observation", ""),
            "result": observation.get("result", {})
        }
    
    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """Get the conversation history"""
        return self.conversation_history
    
    def clear_conversation(self):
        """Clear conversation history"""
        self.conversation_history = []
        self.current_task = None
        self.task_progress = [] 