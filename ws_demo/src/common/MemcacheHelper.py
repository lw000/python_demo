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

class MemcacheHelper(object):
    
    def __init__(self):
        self.__memc = Client(['192.168.204.128:11211'])
      
      
    def getHelper(self):
        return self.__memc
      
class MemcacheHashHelper(object):
    
    def __init__(self):
        self.__memc = HashClient([('192.168.204.128', 11211)]) #('192.168.204.128', 11212),
    
    def getHelper(self):
        return self.__memc
    
def client_test():
    memc = MemcacheHelper()
#     memc = Client(('192.168.204.128', 11211))
    memc.getHelper().set('liwei0', '1111111111111111')
    memc.getHelper().set('counter', 0)
    memc.getHelper().incr('counter', 1)
    print(memc.get('counter'))
    memc.getHelper().set_multi({'name': 'liwei', 'age': 7})
    memc.getHelper().set('liwei1', '2222222222222222')
    memc.getHelper().set('liwei2', '3333333333333333')

    logging.debug(memc.getHelper().get('liwei0'))
    logging.debug(memc.getHelper().get('liwei1'))
    logging.debug(memc.getHelper().get('liwei2'))
    
def hashclient_test():
    client = MemcacheHashHelper()
    client.getHelper().set('heshanshan', 'some value')
    result = client.getHelper().get('heshanshan')   
    logging.debug(client.getHelper().get('heshanshan'))

def main():
    
    hashclient_test()
    
    client_test()
    
if __name__ == '__main__':
#     profile.run('main()')
#     cProfile.run('main()')
    main()