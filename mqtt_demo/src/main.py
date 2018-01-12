'''
Created on 2017年12月29日

@author: Administrator
'''

import sys
import socket
import os
import time
import  getopt
from datetime import datetime
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.gevent import GeventScheduler
import threading

#=======================================================
# MQTT Initialize.--------------------------------------
try:
    import paho.mqtt.client as mqtt
    import paho.mqtt.publish as publish
    import paho.mqtt.subscribe as subscribe
    
except ImportError:
    print('MQTT client not find. Please install as follow:')
    print('git clone http://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git')
    print('cd org.eclipse.paho.mqtt.python')
    print('sudo python setup.py install')

#======================================================

#RPi.GPIO 模块使用基础

__channel_common_000 = '/common/000'
__channel_liwei_000 = '/liwei/000'
__channel_liwei_111 = '/liwei/111'
__channel_heshanshan_000 = '/heshanshan/000'
__channel_heshanshan_111 = '/heshanshan/111'

# __broker = 'localhost'
__broker = '127.0.0.1'

__count = 0

def transmitMQTT(msg = 'this is a test message.'):
    global __count
    msg = msg + str(__count);
    __count += 1
    
    publish.single(topic=__channel_liwei_000, payload=msg, hostname = __broker)
    publish.single(topic=__channel_liwei_111, payload=msg, hostname = __broker)
    publish.single(topic=__channel_heshanshan_000, payload=msg, hostname = __broker)
    publish.single(topic=__channel_heshanshan_111, payload=msg, hostname = __broker)
    
def on_connect(client, userdata, flags, rc):
    print('OnConnetc, rc: ' + str(rc))
    if rc == 0:
        client.publish(topic=__channel_common_000, payload='i\'m python client')

def on_publish(client, obj, mid):
    print('OnPublish, mid: ' + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print('Subscribed: ' + str(mid) + ' ' + str(granted_qos))

def on_log(client, obj, level, string):
    print('Log:' + string)

def on_message(client, obj, msg):
    if msg.topic == __channel_liwei_000 or msg.topic == __channel_liwei_111:
        curtime = datetime.now()
        strcurtime = curtime.strftime('%Y-%m-%d %H:%M:%S')
        print(strcurtime + ': ' + msg.topic + ' ' +
              str(msg.qos) + ' ' + str(msg.payload))
        on_exec(str(msg.payload))
    elif msg.topic == __channel_common_000:
        curtime = datetime.now()
        strcurtime = curtime.strftime('%Y-%m-%d %H:%M:%S')
        print(strcurtime + ': ' + msg.topic + ' ' +
              str(msg.qos) + ' ' + str(msg.payload))

def on_exec(strcmd):
    print('exec:', strcmd)
    strExec = strcmd
  
if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], 'ht:m:')
    s = ''
    m = ''
    for op, v in opts:
        if op == '-t':
            s = v
        elif op == '-m':
            m = v
            
    if s == 's':
        try:
            client = mqtt.Client('mynodeserver')
            client.on_message = on_message
            client.on_connect = on_connect
            client.on_publish = on_publish
            client.on_subscribe = on_subscribe
            client.on_log = on_log
            
            client.connect(__broker)
            
            client.subscribe(topic=__channel_common_000, qos=0)
            client.subscribe(topic=__channel_liwei_000, qos=0)
            client.subscribe(topic=__channel_liwei_111, qos=0)
            
            client.loop_forever()
    
        except (KeyboardInterrupt, SystemExit):
            client.disconnect()
            
    elif s == 'p':
#         sched = BackgroundScheduler()
#         sched.add_job(transmitMQTT, 'interval', seconds=1, args=(m,))  #interval 间隔调度（每隔多久执行）
#         sched.start()
#         try:
#             while True:
#                 time.sleep(10)
#         except (KeyboardInterrupt, SystemExit):
#             sched.shutdown()
 
        sched = GeventScheduler()
        sched.add_job(transmitMQTT, 'interval', seconds=1, args=(m,))
        g = sched.start()
    
        try:
            g.join()
        except (KeyboardInterrupt, SystemExit):
            pass