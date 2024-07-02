from flask import Flask
from flask_cors import CORS
import certifi

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
