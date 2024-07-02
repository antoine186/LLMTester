import ollama
from app.assets.founder_question_scenarios_list import founder_question_scenarios_list
from app.assets.founder_question_generation_guidelines import founder_question_generation_guidelines

def generate_nth_scenario(question_scenario_n):
    
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': founder_question_scenarios_list[question_scenario_n - 1] + founder_question_generation_guidelines,
        },
    ])
    
    return response['message']['content']
