'''
Created on 2017年12月28日

@author: Administrator
'''

import requests
import json
import time

def main():
    url = 'http://localhost:4000/jsonrpc'
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        'method': 'echo',
        'params': ['echome!'],
        'jsonrpc': '2.0',
        'id': 0,
    }
    
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

#     assert response['result'] == 'echome!'
#     assert response['jsonrpc']
#     assert response['id'] == 0
    
    print(response['result'])
    print(response['jsonrpc'])
    print(response['id'])
    
    
    for i in range(5):
        t = time.time()
        payload = {
            'method': 'add',
            'params': [1,2],
            'jsonrpc': '2.0',
            'id': 1,
        }
        
        response = requests.post(
            url, data=json.dumps(payload), headers=headers).json()
        t1 = time.time()
        print(t1 - t)
        print(response['result'])
        print(response['jsonrpc'])
        print(response['id'])
        
        
if __name__ == '__main__':
    main()
