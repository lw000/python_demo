#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017年12月20日

@author: Administrator
'''
import sys
import pycos
import socket
import threading
   
def method():
    if sys.version_info.major > 2:
        read_input = input
    else:
        read_input = raw_input
        
    thread_pool = pycos.AsyncThreadPool(4)
    while True:
        line = yield thread_pool.async_task(read_input)
        line = line.strip()
        print(threading.current_thread(), line)

def client_recv(sock, sender, task=None):
    while True:
        line = yield sock.recv_msg()
        if not line:
            sender.terminate()
            break
        print(line.decode())

def client_send(sock, task=None):
    # since readline is synchronous (blocking) call, use async thread
    thread_pool = pycos.AsyncThreadPool(1)
    if sys.version_info.major > 2:
        read_input = input
    else:
        read_input = raw_input
    while True:
        try:
            line = yield thread_pool.async_task(read_input)
            line = line.strip()
            if line in ('quit', 'exit'):
                break
        except:
            break
        yield sock.send_msg(line.encode())
            
if __name__ == '__main__':
    sender = pycos.Task(method)
    sender.value()
    
#     sender.terminate()
    
    # optional arg 1 is host IP address and arg 2 is port to use
#     host, port = 'localhost', 3456
#     if len(sys.argv) > 1:
#         host = sys.argv[1]
#     if len(sys.argv) > 2:
#         port = int(sys.argv[2])
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # in other programs socket is converted to asynchronous and 'connect' is
#     # used with 'yield' for async I/O. Here, for illustration, socket is first
#     # connected synchronously (since 'yield' can not be used in 'main') and then
#     # it is setup for asynchronous I/O
#     sock.connect((host, port))
#     sock = pycos.AsyncSocket(sock)
#     sender = pycos.Task(client_send, sock)
#     recvr = pycos.Task(client_recv, sock, sender)
#     sender.value()
#     recvr.terminate()