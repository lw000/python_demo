# -*- coding: UTF-8 -*-

'''
Created on 2017年12月19日

@author: Administrator
'''

import gevent
from gevent.event import Event
from gevent.event import AsyncResult
from gevent.queue import Queue
# from gevent.lock.RLock import RLock
# from gevent.lock.Semaphore import Semaphore

evt = Event()
a = AsyncResult()
tasks = Queue()

# def setter():
#     '''After 3 seconds, wake all threads waiting on the value of evt'''
#     print('A: Hey wait for me, I have to do something')
#     gevent.sleep(3)
#     print("Ok, I'm done")
#     evt.set()
# 
# def waiter():
#     '''After 3 seconds the get call will unblock'''
#     print("I'll wait for you")
#     evt.wait()  # blocking
#     print("It's about time")
# 
# def asetter():
#     """
#     After 3 seconds set the result of a.
#     """
#     gevent.sleep(3)
#     a.set('Hello!')
# 
# def awaiter():
#     """
#     After 3 seconds the get call will unblock after the setter
#     puts a value into the AsyncResult.
#     """
#     print(a.get())
# 
# 
# def worker(n):
#     while not tasks.empty():
#         task = tasks.get()
#         print('Worker %s got task %s' % (n, task))
#         gevent.sleep(0)
# 
#     print('Quitting time!')
# 
# def boss():
#     for i in range(1,25):
#         tasks.put_nowait(i)
# 
# def main():
#     gevent.spawn(boss).join()
#     gevent.joinall([
#         gevent.spawn(setter),
#         gevent.spawn(waiter),
#         gevent.spawn(waiter),
#         gevent.spawn(asetter),
#         gevent.spawn(awaiter),
#         gevent.spawn(awaiter),
#         gevent.spawn(worker, 'steve'),
#         gevent.spawn(worker, 'john'),
#         gevent.spawn(worker, 'nancy'),
#     ])

def test(**kwargs):
    name = kwargs['name']
    while True:
        print('%s say: begin ++++++++++++++++++' % name)
        gevent.sleep(1)
        print('%s say: end ++++++++++++++++++' % name)

def test1(**kwargs):
    name = kwargs['name']
    while True:
        print('%s say: begin -----------------' % name)
        gevent.sleep(1)
        print('%s say: end -----------------' % name)

def main():
    gevent.joinall([
        gevent.spawn(test, name='liwei_0000'),
        gevent.spawn(test1, name='liwei_1111')])
    
if __name__ == '__main__':
    main()