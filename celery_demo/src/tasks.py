'''
Created on 2017年12月25日

@author: Administrator
'''
import time
from celery import Celery

broker = 'redis://192.168.204.128:6379/5'
backend = 'redis://192.168.204.128:6379/6'

app = Celery('tasks', broker=broker, backend=backend)

@app.task
def add(x, y):
    return x+y

@app.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')