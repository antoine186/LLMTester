from flask import make_response
from bson import json_util

def cors_preflight_or_inflight_request_response_make(operation_response):
    response = make_response(json_util.dumps(operation_response))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    
    return response
