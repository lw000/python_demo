#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017年 12月15日

@author: Administrator
'''

import redis

import _thread
import threading
import time
import json
import queue
import logging
import schedule

from RedisHelper import RedisHelper

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s %(filename)s[line:%(lineno)d]',
                    datefmt='%a, %d %b %Y %H:%M:%S')

task_queue = queue.Queue()

def radis_push_server(name):
    redis = RedisHelper()
    while True:
        data = {'name': 'liwei', 'age': 30, 'sex': 1, 'addr': '深圳市南山区'}
        j = json.dumps(data, ensure_ascii=False)
        redis.publish(j)  # 发布

        time.sleep(1)

def redis_recved_data_server(name, q):
    redis = RedisHelper()
    redis_sub = redis.subscribe()  # 调用订阅方法
    while True:
        msg = redis_sub.parse_response()
        print('%s-%s' % (name, msg))
        q.put(msg)

class Worker(threading.Thread):

    def __init__(self, q, name):
        self.__quit = False
        self.__q = q
        super(Worker, self).__init__(name=name)

    def quitWorker(self):
        self.__quit = True

    def run(self):
        threading.Thread.run(self)
        while not self.__quit:
            data = self.__q.get()
            print('%s: %s' % (self.name, data[0].decode('utf8')))
            print('%s: %s' % (self.name, data[1].decode('utf8')))
            print('%s: %s' % (self.name, data[2].decode('utf8')))


def worker_server(q, name):
    while True:
        data = q.get()
        print('%s: %s' % (name, data[0]))
        print('%s: %s' % (name, data[1]))
        print('%s: %s' % (name, data[2].decode('utf8')))


def main():
    pool = redis.ConnectionPool(host='192.168.204.128', port=6379)
    r = redis.Redis(connection_pool=pool)
    r.set('liwei', '20')
    print(r.get('liwei').decode())

    try:
#         _thread.start_new_thread(radis_push_server, ('radis_push_server',))
        
        schedule.every(1).seconds.do(radis_push_server, ('radis_push_server'))
        
        t = threading.Thread(target=redis_recved_data_server,
                             name='redis_recved_data_server', args=('redis_recved_data_server', task_queue))
        t.start()

        worker1 = Worker(task_queue, 'worker1')
        worker1.start()

        worker2 = Worker(task_queue, 'worker2')
        worker2.start()

        while True:
            schedule.run_pending()
            time.sleep(1)
            
    except:
        print('error: unable to start thread')

    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()
