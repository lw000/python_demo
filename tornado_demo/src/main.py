'''
Created on 2018年1月10日

@author: Administrator
'''

from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop
import socket
import time
import getopt
import sys
  
HOST = '127.0.0.1'    # The remote host  
PORT = 8000           # The same port as used by the server

def client(): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect((HOST, PORT))  
      
    s.sendall('Hello, \nw'.encode())
    time.sleep(5)
    s.sendall('ord! \n'.encode())
      
    data = s.recv(1024)
      
    print('Received', repr(data))  
      
    time.sleep(60)  
    s.close()

class Connection(object):
    
    clients = set()
    
    def __init__(self, stream, address):
        Connection.clients.add(self)
        self._stream = stream
        self._address = address
        self._stream.set_close_callback(self.on_close)
        self.read_message()
        print("A new user has entered the chat room.", address)
    
    def read_message(self):    
        self._stream.read_until('\n', self.broadcast_messages)
    
    def broadcast_messages(self, data):
        print("User said:", data[:-1], self._address)
        for conn in Connection.clients:
            conn.send_message(data)
        self.read_message()
        
    def send_message(self, data):
        self._stream.write(data)
            
    def on_close(self):    
        print("A user has left the chat room.", self._address)
        Connection.clients.remove(self)

class ChatServer(TCPServer):
    
    def handle_stream(self, stream, address):
        print("New connection :", address, stream)   
        Connection(stream, address)
        print("connection num is:", len(Connection.clients))
    
if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], 'ht:')
    t = ''
    for op, v in opts:
        if op == '-t':
            t = v

    if t == 's':
        try:
            server = ChatServer()
            server.bind(8000)
    #         server.start(0)  # Forks multiple sub-processes
            IOLoop.current().start()
        except KeyboardInterrupt:
            pass
    elif t == 'c':
        try:
            client()
        except KeyboardInterrupt:
            pass