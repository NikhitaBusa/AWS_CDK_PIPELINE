import json
from main import lambda_handler

body = {}
event = json.dumps(body)
lambda_handler(None, None)
print("Hello")
