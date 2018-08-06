import os
#import requests
import json


class ANS(object):
    
    def __init__(self):
        self.ans_url = 'https://api.aceinna.com/api'

    def setStatus(self):
        data = {}
        url = self.ans_url + "/replaceOrCreate"
        data_json = json.dumps(data)
        headers = {'Content-type': 'application/json', 'Authorization' : '' }
        #response = requests.post(url, data=data_json, headers=headers)
        #response = response.json()
        
    
    