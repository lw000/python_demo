# -*- coding=utf-8 -*-
'''
Created on 2017年12月18日

@author: Administrator
'''

import socket
import socketserver
import getopt
import sys
import time
from ctypes.test.test_errno import threading

class EchoServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

    def __init__(self, server_address, RequestHandlerClass):
            socketserver.ThreadingTCPServer.__init__(self, server_address, RequestHandlerClass)


class handler(socketserver.StreamRequestHandler):
    
    def handle(self):
        socketserver.BaseRequestHandler.handle(self)
        self.__conn = self.request

        while True:
            recv_bytes = self.__conn.recv(1024)
            str_bytes = str(recv_bytes, encoding='utf8')
            print('recv: ', str_bytes, threading.current_thread().ident)
            if str_bytes == 'q':
                break
            self.__conn.send(bytes(str_bytes, encoding='utf-8'))

def main_server():
    serv = EchoServer(('127.0.0.1', 9000), handler)
    serv.serve_forever()

def main_client():
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9000))

    while True:
        inp = input('input:\n >>>')
        if inp == 'q':
            break
        client.send(bytes(inp.upper(), encoding='utf-8'))
        ret_bytes = client.recv(1024)
        ret_str = str(ret_bytes, encoding='utf-8')
        print('recv: ', ret_str)

def main():
    opts, _ = getopt.getopt(sys.argv[1:], 'ht:')
    t = ''
    for op, v in opts:
        if op == '-t':
            t = v

    if t == 's':
        main_server()
    elif t == 'c':
        main_client()
    
    print('cammand parameter error xxxx.py (-t s) or (-t c).')

if __name__ == '__main__':
    main()
