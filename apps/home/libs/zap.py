import time
from zapv2 import ZAPv2
import json
import requests







def run_test(zaper,test):

    apiKey = zaper['config_api_key']
    endpoint = zaper['config_endpoint']
    target = test['test_url']
    zap = ZAPv2(apikey=apiKey, proxies={'http': endpoint, 'https': endpoint})
    

    try:
        scanID = zap.spider.scan(url=target)
        while int(zap.spider.status(scanID)) < 100:
                time.sleep(1)

        scanID = zap.ascan.scan(target)

        url = 'http://localhost:5000/zap'
        request_data = {'success':scanID, 'test':test['id']}
        json_data = json.dumps(request_data)
     
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json_data, headers=headers)
        
        
        return {"success":response}
    except:
         return {"error":"Zap not Connected"}
    


def check_status(zaper,test):

    apiKey = zaper['config_api_key']
    endpoint = zaper['config_endpoint']

    zap = ZAPv2(apikey=apiKey, proxies={'http': endpoint, 'https': endpoint})

    try:
        progress = zap.ascan.status(test['zap_id'])
        if(progress=="100"):
            results = zap.core.alerts(baseurl=test['test_url'])
            return {"success":["100",results]}
        return {"success":[progress,""]}
    except:
         return {"error":"Zap not Connected"}
