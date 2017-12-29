#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017年 12月15日

@author: Administrator
'''

import websocket
import _thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print('### closed ###')

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send('Hello %d' % i)
        time.sleep(1)
        ws.close()
        print('thread terminating...')
        
    _thread.start_new_thread(run, ())


if __name__ == '__main__':
#     websocket.enableTrace(True)
    ws = websocket.WebSocketApp('ws://192.168.204.128:3000/',
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
