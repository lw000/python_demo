#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017年 12月15日

@author: Administrator
'''

import memcache

from pymemcache.client.base import Client
from pymemcache.client.hash import HashClient

import logging
import profile
import cProfile

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s %(filename)s[line:%(lineno)d]',
                    datefmt='%a, %d %b %Y %H:%M:%S') #, filename='memcached_demo.log'

def main_client_test():
    memc = memcache.Client(['192.168.204.128:11211'])
#     memc = Client(('192.168.204.128', 11211))
    memc.set('liwei0', '1111111111111111')
    memc.set('counter', 0)
    memc.incr('counter', 1)
    print(memc.get('counter'))
    memc.set_multi({'name': 'liwei', 'age': 7})
    memc.set('liwei1', '2222222222222222')
    memc.set('liwei2', '3333333333333333')

    logging.debug(memc.get('liwei0'))
    logging.debug(memc.get('liwei1'))
    logging.debug(memc.get('liwei2'))
    
    
def main_hashclient_test():
    client = HashClient([('192.168.204.128', 11211)]) #('192.168.204.128', 11212),
    client.set('heshanshan', 'some value')
    result = client.get('heshanshan')
    
    logging.debug(client.get('heshanshan'))


def main():
    
    main_hashclient_test()
    
    main_client_test()
    
if __name__ == '__main__':
#     profile.run('main()')
#     cProfile.run('main()')
    main()