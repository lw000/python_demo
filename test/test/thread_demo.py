# -*- coding: UTF-8 -*-

'''
Created on 2017年12月14日

@author: Administrator
'''

# import _thread
import threadpool
import threading
import time
import wget
import logging
import queue
import schedule

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s %(filename)s[line:%(lineno)d]',
                    datefmt='%a, %d %b %Y %H:%M:%S')

worker_queue = queue.Queue(-1)
lifo_worker_queue = queue.LifoQueue(-1)

cond = threading.Condition()


def down_url(url):
    filename = wget.download(url)
    print(filename)


def hello():
    print('hello')


class Consumer(threading.Thread):
    
    def __init__(self, q, cond, name):
        self.__q = q
        self.__cond = cond
        super(Consumer, self).__init__(name=name)
        
    def run(self):
        threading.Thread.run(self)
        while True:
#             self.__cond.acquire()
#             if self.__q.empty():
#                 self.__cond.wait()
            v = self.__q.get()
            print(self.name + ' [%d] >>>>>>>> %d' % (self.ident, v))
#             self.__cond.release()

class Producer(threading.Thread):
    
    def __init__(self, q, name):
        self.__q = q
        super(Producer, self).__init__(name=name)
        
    def run(self):
        threading.Thread.run(self)
        while True:
            for i in range(10):
                self.__q.put(i)
            
            time.sleep(2)
        
def get_task(q, name):

    while True:
        v = q.get()
        print(name + ' [%d] >>>>>>>> %d' % (threading.currentThread().ident, v))


def put_task(q):
    for i in range(10):
        q.put(i)
#         time.sleep(1)


def test(name):
    print(11111111111)

    
if __name__ == '__main__':
    try:
#         _thread.start_new_thread(down_url, ('http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3',))

        timer = threading.Timer(3, hello)
        timer.start()
        
#         t1 = threading.Thread(target=put_task,
#                               name='put_task', args=(worker_queue, 'put_task'))
#         t1.start()
        
        consumer = Consumer(worker_queue, cond, 'consumer')
        consumer.start()
        
        consumer1 = Consumer(worker_queue, cond, 'consumer1')
        consumer1.start()
        
        schedule.every(1).seconds.do(put_task, (worker_queue))
        
#         schedule.every(1).minutes.do(put_task, (worker_queue, 'put_task'))
#         schedule.every(1).hour.do(put_task, (worker_queue, 'put_task'))
#         schedule.every(1).day.at("10:30").do(put_task, (worker_queue, 'put_task'))
#         schedule.every(1).monday.do(put_task, (worker_queue, 'put_task'))
#         schedule.every(1).wednesday.at("13:15").do(put_task, (worker_queue, 'put_task'))
        
#         Producer = Producer(worker_queue, ('producer',))
#         Producer.start()
        
#         pool = threadpool.ThreadPool(2)
#         request = threadpool.makeRequests(get_task,
#             [(None, {'q': worker_queue, 'name': 'get_task'}),
#               (None, {'q': worker_queue, 'name': 'get_task'})])
#         for req in request:
#             pool.putRequest(req)
#         pool.wait()
        
        while True:
            schedule.run_pending()
            time.sleep(1)
                
    except:
        logging.debug('error: unable to start thread')
