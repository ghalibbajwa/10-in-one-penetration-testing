import burpsuite
import json
import requests


def run_test(burp, test):
    

    SERVER_URL = burp['config_endpoint']
    API_KEY = burp['config_api_key']
    burp_api_client = burpsuite.BurpSuiteApi(server_url=SERVER_URL, api_key=API_KEY)
    
    
    if(test['site_username'] != '' and test['site_password'] != ''):
        options = {
        "scan_configurations":[{"name":"Crawl and Audit - Lightweight","type":"NamedConfiguration"}],
        "urls": [test['test_url']],
        "application_logins": [{"username": test['site_username'], "password": test['site_password']}]
    }
    else:
        options = {
        "scan_configurations":[{"name":"Crawl and Audit - Lightweight","type":"NamedConfiguration"}],
        "urls": [test['test_url']]
    }

    try:
        task_id = burp_api_client.initiate_scan(options=options)
        url = 'http://localhost:5000/burp'
        request_data = {'success':task_id, 'test':test['id']}
        json_data = json.dumps(request_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json_data, headers=headers)
        
        
        return {"success":response}

    except Exception as e:
        return {"error":f'{e}'}


def check_status(burp, test):
    SERVER_URL = burp['config_endpoint']
    API_KEY = burp['config_api_key']
    burp_api_client = burpsuite.BurpSuiteApi(server_url=SERVER_URL, api_key=API_KEY)
    
   

    try:
        progress = burp_api_client.get_scan(task_id=test['burp_id'])
      
        return {"success":progress}

    except Exception as e:
        return {"error":f'{e}'}
    