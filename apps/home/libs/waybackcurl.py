import requests
import sys
import json
from apps.home.libs import secretfinder as sfinder

def waybackurls(host, with_subs):
    if with_subs:
        url = 'http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=json&fl=original&collapse=urlkey' % host
    else:
        url = 'http://web.archive.org/cdx/search/cdx?url=%s/*&output=json&fl=original&collapse=urlkey' % host
    r = requests.get(url)
    results = r.json()
    return results[1:]

def start_secret_finder(test):
    
    urls = waybackurls(test['test_url'], False)
    js_urls=[]
    for url in urls:
        for k in url:
            if('.js' in k):   
                js_urls.append(k)
    

    results=[]
    count=0
    for url in js_urls:
        results.append([url,sfinder.start(url)])
        count+=1
        progress = (count / len(js_urls)) * 100
        
   
        url = 'http://localhost:5000/secretfinder'
        request_data = { 'test':test['id'],'secret_finder_data': ["in progress",progress,results]}
        json_data = json.dumps(request_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json_data, headers=headers)


    url = 'http://localhost:5000/secretfinder'
    request_data = { 'test':test['id'],'secret_finder_data': ["succeeded",progress,results]}
    json_data = json.dumps(request_data)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json_data, headers=headers)
    
    return "OK"