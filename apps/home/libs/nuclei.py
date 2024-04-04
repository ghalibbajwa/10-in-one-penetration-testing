from PyNuclei import Nuclei
import threading
import requests
import json
from urllib.parse import urlparse, urlunparse


def remove_protocol(url):
    url = url.split(":")

    return(url[1][2:])

def run_test(nuceli, test):

    url = remove_protocol(test['test_url'])
  

    
    try:
        nucleiPath = nuceli['config_path']
        

        scan(test['id'],url,nucleiPath)
       
        return {"success":'OK'}

    except Exception as e:
        return {"error":f'{e}'}





def scan(test_id,url,nucleiPath):
    nucleiScanner = Nuclei(nucleiPath)
    
    scanResult = nucleiScanner.scan(
        url,
        templates=["cves", "network", "ssl"],
        rateLimit=150, 
        verbose=True,
        metrics=False,
        maxHostError=30,
        stopAfter=None
    )
   
    url = 'http://localhost:5000/nuclei'
    request_data = {'progress':100, 'status':"succeeded", 'test':test_id,'nuclei_data': scanResult}
    json_data = json.dumps(request_data)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json_data, headers=headers)



