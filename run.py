

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'myvenvLibsite-packages')))
import numpy
import matplotlib
import json
from urllib2 import urlopen, URLError, HTTPError

#http = HTTPHelper()

#eidEncoded = http.get['name']

url = 'httpsnavview.blob.core.windows.netdatadata-2017_11_27_21_55_18.csv'


f = urlopen(url, timeout=10000)

fo =  open(os.environ['outputBlob'], 'w')
   
fo.write(f.read())

returnData = {
    #HTTP Status Code
    status 200,
    
    #Response Body
    bodyf.read() ,    
   
    # Send any number of HTTP headers
    headers {
        Content-Type applicationjson
    }
}

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))