import sys
from AzureToAns import ANS
import os
import json

_AZURE_FUNCTION_DEFAULT_METHOD = "GET"
_AZURE_FUNCTION_HTTP_INPUT_ENV_NAME = "req"
_AZURE_FUNCTION_HTTP_OUTPUT_ENV_NAME = "res"
_REQ_PREFIX = "REQ_"

def write_http_response(status, body_dict):
    return_dict = {
        "status": status,
        "body": json.dumps(body_dict),
        "headers": {
            "Content-Type": "application/json"
        }
    }
    output = open(os.environ[_AZURE_FUNCTION_HTTP_OUTPUT_ENV_NAME], 'w')
    output.write(json.dumps(return_dict))


env = os.environ

# Get HTTP METHOD
http_method = env['REQ_METHOD'] if 'REQ_METHOD' in env else _AZURE_FUNCTION_DEFAULT_METHOD
print("HTTP METHOD => {}".format(http_method))

# Get QUERY STRING
req_url = env['REQ_HEADERS_X-ORIGINAL-URL'] if 'REQ_HEADERS_X-ORIGINAL-URL' in env else ''
urlparts =req_url.split('?') 
query_string = urlparts[1] if len(urlparts) == 2 else ''
print("QUERY STRING => {}".format(query_string))

class JSONObject:
     def __init__(self, d):
         self.__dict__ = d


if http_method.lower() == 'post':
    request_body = open(env[_AZURE_FUNCTION_HTTP_INPUT_ENV_NAME], "r").read()
    if 'userId' in request_body:
        data = json.loads(request_body, object_hook=JSONObject)
        print(data)
        record_to_ansplatform(data)

res_body = {"success": 1}
