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

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s %(filename)s[line:%(lineno)d]',
                    datefmt='%a, %d %b %Y %H:%M:%S')

worker_queue = queue.Queue()


class RedisHelper(object):

    def __init__(self):
        self.__pool = redis.ConnectionPool(host='192.168.204.128', port=6379)
        self.__conn = redis.Redis(connection_pool=self.__pool)
        self.channel = 'monitor'  # 定义名称

    def publish(self, msg):  # 定义发布方法
        self.__conn.publish(self.channel, msg)
        return True

    def subscribe(self):  # 定义订阅方法
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub


def push_server(name):
    obj = RedisHelper()
    while True:
        data = {'name': 'liwei', 'age': 30, 'sex': 1, 'addr': '深圳市南山区'}
        j = json.dumps(data, ensure_ascii=False)
        obj.publish(j)  # 发布

        time.sleep(1)


def sub_server(name, q):
    obj = RedisHelper()
    redis_sub = obj.subscribe()  # 调用订阅方法
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
#         _thread.start_new_thread(push_server, ('push_server',))
        
        schedule.every(1).seconds.do(push_server, ('push_server'))
        
        t = threading.Thread(target=sub_server,
                             name='sub_server', args=('sub_server', worker_queue))
        t.start()

        worker1 = Worker(worker_queue, 'worker1')
        worker1.start()

        worker2 = Worker(worker_queue, 'worker2')
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
