#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017��12��14��

@author: Administrator
'''

import requests
import grequests
import cProfile

urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://fakedomain/',
    'http://kennethreitz.com'
]

def execpt_handler(req, exception):
    print('Request failed')
    
if __name__ == '__main__':
    v = requests.get('https://github.com/timeline.json')
    print(v.content)
    print(v.text)
    
    rs = (grequests.get(u) for u in urls)
    print(grequests.map(rs, exception_handler=execpt_handler))
    
    while True:
        pass