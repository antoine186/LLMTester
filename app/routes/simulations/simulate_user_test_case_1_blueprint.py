from flask import Blueprint, request
import json

from app.utils.cors_preflight_or_inflight_request_response_make import cors_preflight_or_inflight_request_response_make

from app.utils.generate_nth_scenario import generate_nth_scenario
from app.utils.address_founder_question_to_customer_service_chatbot import address_founder_question_to_customer_service_chatbot
from app.utils.generate_unique_string_id import generate_unique_string_id

simulate_user_test_case_1_blueprint = Blueprint('simulate_user_test_case_1_blueprint', __name__)

@simulate_user_test_case_1_blueprint.route('/api/simulate-user-test-case-1-blueprint', methods=['POST', 'OPTIONS'])
def handle_user_query():
    try:
        if request.method == 'OPTIONS':
            response = cors_preflight_or_inflight_request_response_make(operation_response={})
            
            return response
        
        payload = request.data
        payload = json.loads(payload)
        current_conversation_string_id = generate_unique_string_id()
        
        founder_question_1_text = generate_nth_scenario(question_scenario_n=1)
        chatbot_response_1_text = address_founder_question_to_customer_service_chatbot(founder_question_1_text, current_conversation_string_id, payload['data']['chatbot_to_test'])
            
        operation_response = {
            "operation_success": True,
            "return_value": {
                "llm_output": response['message']['content']
                },
            "return_message": ""
        }
        
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
