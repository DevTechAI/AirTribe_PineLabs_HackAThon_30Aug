import openai
import os
from typing import Dict, Any
import json

class AIAssistant:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.model = "gpt-3.5-turbo"
    
    def chat(self, message: str, context: Dict[str, Any] = None) -> str:
        """AI-powered chat assistance for integration questions"""
        try:
            system_prompt = """
            You are an AI assistant specialized in Pine Labs payment API integration.
            Help developers with:
            1. Understanding API endpoints and parameters
            2. Troubleshooting integration issues
            3. Best practices for payment processing
            4. Code examples in various languages
            5. Error resolution
            
            Be concise, practical, and focus on Pine Labs specific integration.
            If you don't know something specific to Pine Labs, say so.
            """
            
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ]
            
            if context:
                context_str = f"Context: {json.dumps(context)}"
                messages.insert(1, {"role": "system", "content": context_str})
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"I apologize, but I'm having trouble processing your request. Error: {str(e)}"
    
    def generate_code(self, language: str, integration_type: str) -> str:
        """Generate code snippets for different integration types"""
        try:
            prompts = {
                'python': {
                    'payment': """
                    Generate Python code for Pine Labs payment integration using requests library.
                    Include proper error handling, payload validation, and response parsing.
                    Use the sandbox environment.
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
                model=self.model,
                messages=messages,
                max_tokens=1000,
                temperature=0.3
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"// Error generating code: {str(e)}"
    
    def fix_error(self, error_message: str, code: str, language: str) -> str:
        """AI-powered error fixing for integration code"""
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
                model=self.model,
                messages=messages,
                max_tokens=1000,
                temperature=0.2
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"// Error fixing code: {str(e)}" 