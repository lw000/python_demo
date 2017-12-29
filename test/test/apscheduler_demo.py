'''
Created on 2017年12月22日

@author: Administrator
'''

import os
import time
from datetime import datetime
from datetime import date
from tornado.ioloop import IOLoop
from apscheduler.schedulers.tornado import TornadoScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.gevent import GeventScheduler

def tick():
    print('Tick()! The time is: %s' % datetime.now())

def tick1():
    print('Tick1()! The time is: %s' % datetime.now())
   
def my_job():
    print('my_job()! The time is: %s' % datetime.now())
       
def BlockingScheduler_test():
    sched = BlockingScheduler()
    sched.add_job(tick, 'interval', seconds=3)
    sched.add_job(tick1, 'cron',second = '*/1')
    
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        pass
    
    
def BackgroundScheduler_test():
    sched = BackgroundScheduler()
    sched.add_job(tick, 'interval', seconds=1)  #interval 间隔调度（每隔多久执行）
    sched.add_job(tick1, 'cron',second = '*/1') #cron定时调度（某一定时时刻执行）
    #表示2017年3月22日17时19分07秒执行该程序
#     sched.add_job(my_job, 'cron', year=2017,month=12, day=22, hour=16, minute=39, second=7)
#     sched.add_job(my_job, 'date', run_date=datetime(2017, 12, 22, 16, 47, 0), args=['text'])
    
    sched.start()
    
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        sched.shutdown()
    
def TornadoScheduler_test():
    sched = TornadoScheduler()
    sched.add_job(tick, 'interval', seconds=3)
    sched.add_job(tick1, 'interval', id = '1', seconds=1)
    sched.start()
    
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        IOLoop.instance().start()
    except (KeyboardInterrupt, SystemExit):
        pass
    
def GeventScheduler_test():
    sched = GeventScheduler()
    sched.add_job(tick, 'interval', seconds=3)
    g = sched.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        g.join()
    except (KeyboardInterrupt, SystemExit):
        pass
       
if __name__ == '__main__':
#     BlockingScheduler_test()
    BackgroundScheduler_test()
#     TornadoScheduler_test()
#     GeventScheduler_test()
    