'''
Created on 2017年12月28日

@author: Administrator
'''

import zerorpc

class HelloRPC(object):
    def hello(self, name):
        return "Hello, %s" % name
    
    def add(self, a, b):
        return a+b
    
    def sub(self, a, b):
        return a-b
    
    def len(self, s):
        return len(s)
    
if __name__ == '__main__':
    s = zerorpc.Server(HelloRPC())
    s.bind("tcp://0.0.0.0:4242")
    s.run()