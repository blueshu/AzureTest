import sys, os
import json
from AzureHTTPHelper import HTTPHelper
from AzureToAns import ANS
# This is a little class used to abstract away some basic HTTP functionality
http = HTTPHelper()

# All these print statements get sent to the Azure Functions live log
print "--- GET ---"
print http.get
print

print "--- POST ---"
print http.post
print

print "--- HEADERS ---"
print http.headers
print


# All data to be returned to the client gets put into this dict
returnData = {
    #HTTP Status Code:
    "status": 200,
    
    #Response Body:
    "body": '{"res":"1222"}',
    
    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }
}

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))