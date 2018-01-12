'''
Created on 2018年1月4日

@author: Administrator
'''

import websocket
import time
import json
import random
import uuid
import gevent
from gevent import monkey
monkey.patch_all()

try:
    import thread
except ImportError:
    import _thread as thread

from chat_pb2 import ChatRequest
from chat_pb2 import ChatReply

# def on_data(ws, message, ty, flag):
#     print(message, ty, flag)

def on_message(ws, message):
    data = json.loads(message)
    name = data['name'];
    rid = data['rid'];
    uid = data['uid'];
    msg = data['msg'];
    d = 'name:%s rid:%s uid:%s say:%s' % (name, rid, uid, msg)
    print(d)
    
def on_error(ws, error):
    print(error)

def on_ping(ws, msg):
    print('on_ping: %s' % msg)

def on_pong(ws, msg):
    print('on_pong: %s' % msg)


def on_close(ws):
    print('### closed ###')

def on_open(ws):
    #     def run(*args):
    #         for i in range(100):
    #             time.sleep(0.1)
    #             ws.send('Hello %d' % i)
    #
    #         time.sleep(1)
    #         ws.close()
    #         print('thread terminating...')
    tm = random.randint(5, 10)
    def run(*args):
        while True:
#             time.sleep(tm)
            gevent.sleep(0.001)
            cmd = random.randint(1,2)
            msg = random.choice(['hello apple', 'hello pear', 'hello peach', 'hello orange', 'hello lemon'])
            msg = dict(cmd=cmd, uuid = uuid.uuid4().hex, name=ws.user['name'], upsd=ws.user['upsd'], rid = ws.user['rid'], uid = ws.user['uid'], tm=time.time(), msg=msg)
            s = json.dumps(msg, ensure_ascii=False)
            ws.send(s)
            
        time.sleep(0.5)
        ws.close()

#     thread.start_new_thread(run, ())
    gevent.spawn(run)


def run_client(**kwargs):
    #     websocket.enableTrace(True)

    name = kwargs['name']
    upsd = kwargs['upsd']
    rid = kwargs['rid']
    uid = kwargs['uid']

    p = 'ws://127.0.0.1:8888/ws?name=%s&upsd=%s&rid=%s&uid=%s&extra=%s' % (
        name, upsd, rid, uid, 'extra')
#     ws = websocket.WebSocketApp(p, on_message=on_message,
#                                 on_error=on_error,
#                                 on_close=on_close,
#                                 on_open=on_open,
#                                 on_ping=on_ping,
#                                 on_pong=on_pong)
#                                 on_data=on_data)

    ws = websocket.WebSocketApp(p)
    
    ws.user = {}
    ws.user['name'] = name
    ws.user['upsd'] = upsd
    ws.user['rid'] = rid
    ws.user['uid'] = uid
    
    ws.on_open = on_open
    ws.on_message = on_message
    ws.on_close = on_close
    ws.on_ping = on_ping
    ws.on_pong = on_pong
#     ws.on_data = on_data
    
    ws.run_forever(ping_interval=30)


if __name__ == '__main__':
    s = ChatRequest()
    s.from_uid = 10000
    s.to_uid = 10001
    s.msg = '1000'
    d = s.SerializeToString()

    s1 = ChatRequest()
    s1.ParseFromString(d)

    r = ChatReply()
    r.from_uid = 10000
    r.to_uid = 10001
    r.msg = '1000'
    d1 = r.SerializeToString()

    r1 = ChatRequest()
    r1.ParseFromString(d)
    
#     gevent.joinall([gevent.spawn(run_client, name='liwei_10000', upsd='123456', rid='1', uid='10000'),
#                     gevent.spawn(run_client, name='liwei_10001', upsd='123456', rid='1', uid='10001')])
    
    gevent.joinall([gevent.spawn(run_client, name='liwei_10000', upsd='123456', rid='1', uid='10000'),
                    gevent.spawn(run_client, name='liwei_10001', upsd='123456', rid='1', uid='10001'),
                    gevent.spawn(run_client, name='liwei_10002', upsd='123456', rid='2', uid='10002'),
                    gevent.spawn(run_client, name='liwei_10003', upsd='123456', rid='2', uid='10003'),
                    gevent.spawn(run_client, name='liwei_10004', upsd='123456', rid='3', uid='10004'),
                    gevent.spawn(run_client, name='liwei_10005', upsd='123456', rid='3', uid='10005'),
                    gevent.spawn(run_client, name='liwei_10006', upsd='123456', rid='4', uid='10006'),
                    gevent.spawn(run_client, name='liwei_10007', upsd='123456', rid='4', uid='10007'),
                    gevent.spawn(run_client, name='liwei_10008', upsd='123456', rid='1', uid='10008'),
                    gevent.spawn(run_client, name='liwei_10009', upsd='123456', rid='1', uid='10009'),
                    gevent.spawn(run_client, name='liwei_10010', upsd='123456', rid='2', uid='10010'),
                    gevent.spawn(run_client, name='liwei_10011', upsd='123456', rid='2', uid='10011'),
                    gevent.spawn(run_client, name='liwei_10012', upsd='123456', rid='3', uid='10012'),
                    gevent.spawn(run_client, name='liwei_10013', upsd='123456', rid='3', uid='10013'),
                    gevent.spawn(run_client, name='liwei_10014', upsd='123456', rid='4', uid='10014'),
                    gevent.spawn(run_client, name='liwei_10015', upsd='123456', rid='4', uid='10015'),])
        
#     thread.start_new_thread(run_client, kwargs={'name':'liwei_10001', 'upsd':'123456', 'rid':'1', 'uid':'10001'})
#     thread.start_new_thread(run_client, kwargs={'name':'liwei_10002', 'upsd':'123456', 'rid':'1', 'uid':'10002'})
#     thread.start_new_thread(run_client, kwargs={'name':'liwei_10003', 'upsd':'123456', 'rid':'1', 'uid':'10003'})
#     thread.start_new_thread(run_client, kwargs={'name':'liwei_10004', 'upsd':'123456', 'rid':'1', 'uid':'10004'})

#     run_client()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        pass