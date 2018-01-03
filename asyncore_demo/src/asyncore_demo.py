#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017年12月18日

@author: Administrator
'''

import sys
import getopt
import time
import asyncore
import socket
import threading

class EchoHandler(asyncore.dispatcher_with_send):
    
    def __init__(self, name, sock):
        asyncore.dispatcher_with_send.__init__(self, sock)
        self.name = name   
        
    def handle_read(self):
            bydata = self.recv(1024)
            d = bydata.decode()
            if d:
                self.send(d.encode())

class EchoServer(asyncore.dispatcher):
    clients = []
    
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        conn, addr = self.accept()
        handler = EchoHandler('client', conn)
        self.clients.append(handler)
        print('Incoming connection from %s' % repr(addr))
                
    def handle_close(self):
        print('handle_close')
    
    def handle_read(self):
        print('handle_read')
        
    def handle_write(self):
        print('handle_write')
    
class EchoClient(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))

    def handle_connect(self):
        print('handle_connect')

    def handle_close(self):
        print('handle_close')
        self.close()

    def handle_read(self):
            data = self.recv(1024)
            print(data.decode())
            
    def handle_write(self):
            data = '111111111111'
            self.send(data.encode())
        
            
class EchoServerThread(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        
    def run(self):
        self.server = EchoServer(self.host, self.port)
        asyncore.loop()
        
    def close(self):
        self.server.close()


class EchoClientThread(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port

    def run(self):
        self.client = EchoClient(self.host, self.port)
        asyncore.loop()
    
    def close(self):
        self.client.close()

if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], 'ht:')
    t = ''
    for op, v in opts:
        if op == '-t':
            t = v
    
    if t == 's':
        th = EchoServerThread('localhost', 9999)
    elif t == 'c':
        th = EchoClientThread('localhost', 9999)
        
    th.start()
     
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        th.close()
    