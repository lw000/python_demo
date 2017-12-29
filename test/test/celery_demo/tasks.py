'''
Created on 2017年12月25日

@author: Administrator
'''
import time
from celery import Celery

celery = Celery('tasks', broker='redis://192.168.204.128:6379/0')

@celery.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')
    
@celery.task
def add(x, y):
    print(x, y)
    return x+y