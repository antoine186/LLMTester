from flask import Blueprint, request
import ollama

from app.utils.cors_preflight_or_inflight_request_response_make import cors_preflight_or_inflight_request_response_make

simulate_user_test_case_1_blueprint = Blueprint('simulate_user_test_case_1_blueprint', __name__)

@simulate_user_test_case_1_blueprint.route('/api/simulate-user-test-case-1-blueprint', methods=['POST', 'OPTIONS'])
def handle_user_query():
    try:
        if request.method == 'OPTIONS':
            response = cors_preflight_or_inflight_request_response_make(operation_response={})
            
            return response
             
        payload = request.data
        
        response = ollama.chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': 'Why is the sky blue?',
            },
        ])
            
        operation_response = {
            "operation_success": True,
            "return_value": {
                "llm_output": response['message']['content']
                },
            "return_message": ""
        }
        
        """
        operation_response = {
            "operation_success": True,
            "return_value": {
                "llm_output": "Hi"
                },
            "return_message": ""
        }
        """
        
        response = cors_preflight_or_inflight_request_response_make(operation_response)
        return response
    
    except Exception as e:     
        operation_response = {
            "operation_success": False,
            "error_message": str(e),
            "return_message": "has_backend_error"
        }
        
        response = cors_preflight_or_inflight_request_response_make(operation_response)
        return response
