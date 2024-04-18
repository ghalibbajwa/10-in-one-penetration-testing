from apps.home.libs.CMSScan.plugins.scanners import (
    update_wpscan,
    find_cms
)
from apps.home.libs.CMSScan import core
from threading import Thread
import json
import requests


def run_test(test):
    url = test['test_url']
    cms = find_cms(url)
    data=""
    if cms == "unknown":
        data = {"error": "Cannot Detect CMS"}
    else:
       
        data = core.scan(test['id'],cms,url)


    url = 'http://localhost:5000/cmsscan'
    request_data = { 'test':test['id'],'cmsscan_data': ["succeeded",100,data]}
    json_data = json.dumps(request_data)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json_data, headers=headers)