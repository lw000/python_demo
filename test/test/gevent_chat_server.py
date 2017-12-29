# -*- coding: UTF-8 -*-

'''
Created on 2017年12月19日

@author: Administrator
'''

import socket
import getopt
import sys
import gevent
from gevent.queue import Queue
from gevent.server import StreamServer

users = {}  # mapping of username -> Queue

def broadcast(msg):
    msg += '\n'
    for v in users.values():
        v.put(msg)

def reader(username, f):
    for l in f:
        msg = '%s> %s' % (username, l.strip())
        broadcast(msg)


def writer(q, sock):
    while True:
        msg = q.get()
        sock.sendallbytes(msg, encoding='utf-8')


def read_name(f, sock):
    while True:
        sock.sendall(bytes('Please enter your name: ', encoding='utf-8'))
        name = f.readline().strip()
        if name:
            if name in users:
                sock.sendall(bytes('That username is already taken.\n', encoding='utf-8'))
            else:
                return name

def handle(sock, client_addr):
    f = sock.makefile()

    name = read_name(f, sock)

    broadcast('## %s joined from %s.' % (name, client_addr[0]))

    q = Queue()
    users[name] = q

    try:
        r = gevent.spawn(reader, name, f)
        w = gevent.spawn(writer, q, sock)
        gevent.joinall([r, w])
    finally:
        del(users[name])
        broadcast('## %s left the chat.' % name)

def main_server():
#     try:
#         myip = sys.argv[1]
#     except IndexError:
#         myip = '127.0.0.1'
#     
    myip = '127.0.0.1'
    print('To join, telnet %s 8001' % myip)
    s = StreamServer((myip, 8001), handle)
    s.serve_forever()
    
def main_client():
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8001))

    while True:
        inp = input('input:\n >>>')
        if inp == 'q':
            break
        client.send(bytes(inp.upper(), encoding='utf-8'))
        ret_bytes = client.recv(1024)
        ret_str = str(ret_bytes, encoding='utf-8')
        print('recv: ', ret_str)
        
if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], 'ht:')
    t = ''
    for op, v in opts:
        if op == '-t':
            t = v

    if t == 's':
        main_server()
    elif t == 'c':
        main_client()
        
    