import requests
from config import chatbot_1_url, chatbot_2_url
from app.assets.testing_api_headers import headers
import json

def address_founder_question_to_customer_service_chatbot(founder_question_text, conversation_id, chatbot_to_test):
    if chatbot_to_test == 1:
        chatbot_url_currently_tested = chatbot_1_url
    else:
        chatbot_url_currently_tested = chatbot_2_url
    
    chatbot_test_payload = {
        "conversation_id": conversation_id,
        "message": founder_question_text
    }
    
    response = requests.post(chatbot_url_currently_tested, headers=headers, json=chatbot_test_payload)
    response_dict = json.loads(response.text)
    
    return response_dict['response']
