#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017年12月14日

@author: Administrator
'''

import queue
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s %(filename)s[line:%(lineno)d]',
                    datefmt='%a, %d %b %Y %H:%M:%S',filename="TaskQueue.log")

class TaskQueue(object):
     
    def __init__(self):
        self.__queue = queue.Queue(-1)
    
    def addTask(self):
        pass
    
    def removeTask(self):
        pass
    
if __name__ == '__main__':
    pass