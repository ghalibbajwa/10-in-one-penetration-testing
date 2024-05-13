import os
import threading
import json
import requests
import gvm
from gvm.protocols.latest import Gmp
import xmltodict


def remove_protocol(url):
    if(url[-1]=="/" or url[-1]=='\\'):
            url=url[:-1]
    url = url.split(":")

    return(url[1][2:])


def run_test(openvas, test):
            # try:
                endpoint = openvas
                connection = gvm.connections.TLSConnection(hostname=endpoint,port=9390)

                gmp = Gmp(connection)

                gmp.authenticate('admin', 'admin')

                scanner=gmp.get_scanners()
                scanner=xmltodict.parse(scanner)
                scanner = scanner['get_scanners_response']['scanner'][1]["@id"]


              
                target_name = test['test_name']
                hosts = [remove_protocol(test['test_url'])]  # Example: range of IP addresses
                port_range="1000-9999"
                comment = "This is my target for testing purposes"


                target_id = gmp.create_target(name=target_name, hosts=hosts, comment=comment,port_range=port_range)
                target_id =xmltodict.parse(target_id)
              
                target_id = target_id['create_target_response']['@id']
               
                config=gmp.get_scan_configs()
                config=xmltodict.parse(config)
                config = config['get_configs_response']['config'][3]['@id']

                
                task_name = test['test_name']
                # Replace with the actual target ID
                scan_config_id = config  # Example Scan Config ID (replace with your desired scan config ID)

                # Create the scan task
                task_id = gmp.create_task(name=task_name, target_id=target_id, config_id=scan_config_id,scanner_id=scanner)

                task_id= xmltodict.parse(task_id)

                task_id = task_id['create_task_response']['@id']

                report_id = gmp.start_task(task_id)
                report_id = xmltodict.parse(report_id)

             
                report_id = report_id['start_task_response']['report_id']
                url = 'http://localhost:5000/openvas'
                request_data = {'progress':0, 'status':"in Progress", 'test':test['id'],'openvas_data': None,'report_id':report_id}
                print(request_data)
                json_data = json.dumps(request_data)
                headers = {'Content-Type': 'application/json'}
                response = requests.post(url, data=json_data, headers=headers)
           
                return {"success":'OK'}

            # except Exception as e:
            #     return {"error":f'{e}'}




def check_progress(openvas,report_id):
        endpoint = openvas
        connection = gvm.connections.TLSConnection(hostname=endpoint,port=9390)

        gmp = Gmp(connection)

        gmp.authenticate('admin', 'admin')


        report=gmp.get_report(report_id=report_id)
        report=xmltodict.parse(report)
        return report