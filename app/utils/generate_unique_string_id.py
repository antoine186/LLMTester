import random
import string

def generate_unique_string_id(length=10):
    characters = string.ascii_letters + string.digits
    unique_id = ''.join(random.choices(characters, k=length))
    
    return unique_id
