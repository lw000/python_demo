#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017年12月18日

@author: Administrator
'''

import asyncio
import threading

def print_f(s):
    print('%s Hello world! (%s)' % (s, threading.current_thread()))
    return s
    
@asyncio.coroutine
def hello(s):
    print('%s Hello world! (%s)' % (s, threading.current_thread()))
    
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)

    print('%s Hello again! (%s)' % (s, threading.current_thread()))
    return s

@asyncio.coroutine
def hello1(s):
#     while True:       
        print('%s Hello world! (%s)' % (s, threading.current_thread()))
        yield from asyncio.sleep(0.1)
#         yield from print_f(s)
    
@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()
        
if __name__ == '__main__':
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
#     tasks = [asyncio.ensure_future(hello('111')), asyncio.ensure_future(hello('222'))];

    tasks = [];
    
    for i in range(10):
        tasks.append(hello1('hello1-'.join(str(i))))
#         tasks.append(wget('www.baidu.com'))
        
    loop.run_until_complete(asyncio.wait(tasks))
#     loop.run_forever()

#     for task in tasks:
#         print(task.result())
        
    loop.close()