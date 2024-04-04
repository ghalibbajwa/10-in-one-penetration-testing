import os
import threading
import json
import requests


def run_test(nikto, test):
            try:
                path = nikto['config_path']

                current_path = os.getcwd()
                cmd='echo "N" | perl '+ path +' -host '+test['test_url']+' -o '+current_path+'/apps/results/'+ str(test['id']) +'.json'
                
                run_nikto(cmd,str(test['id']) +'.json',test['id'])
           
                return {"success":'OK'}

            except Exception as e:
                return {"error":f'{e}'}



def run_nikto(cmd,filename,test):
       
        os.system(cmd)
        current_path = os.getcwd()+'/apps/results/'+filename
        with open(current_path, 'r') as file:
            data = json.load(file)

        url = 'http://localhost:5000/nikto'
        request_data = {'progress':100, 'status':"succeeded", 'test':test,'nikto_data': data}
        json_data = json.dumps(request_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json_data, headers=headers)
        



