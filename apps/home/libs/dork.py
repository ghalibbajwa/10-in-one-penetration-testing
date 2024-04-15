from apps.home.libs.Dorks import pagodo
import json
import requests

def start_dork(test):


    pg = pagodo.Pagodo(
    google_dorks_file="apps/home/libs/Dorks/dorks2.txt",
    domain=test['test_url'],
    max_search_result_urls_to_return_per_dork=3,
    save_pagodo_results_to_json_file=None,  # None = Auto-generate file name, otherwise pass a string for path and filename.
    save_urls_to_file=None,  # None = Auto-generate file name, otherwise pass a string for path and filename.
    verbosity=5,
)
    



    pagodo_results_dict = pg.go()

    pagodo_results_dict.keys()

    pagodo_results_dict["initiation_timestamp"]

    pagodo_results_dict["completion_timestamp"]


    url = 'http://localhost:5000/dork'
    request_data = { 'test':test['id'],'dork_data': ["succeeded",100,pagodo_results_dict]}
    json_data = json.dumps(request_data)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json_data, headers=headers)

