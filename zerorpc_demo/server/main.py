'''
Created on 2017年12月28日

@author: Administrator
'''
import sys
import getopt
import zerorpc
import time

from CommonModuleServer import CommonModuleServer
    
def client():
    c = zerorpc.Client()
    c.connect('tcp://127.0.0.1:4242')

    for _ in range(10):
        t = time.clock()
        async_result = c.hello('RPC', async=True)
        print(async_result.get(), '--------->', time.clock() - t)
        
        t = time.clock()
        async_result = c.add(1, 2)
        print(async_result, '--------->', time.clock() - t)
        
        t = time.time()
        async_result = c.len('aaaaaaaaaaaaa')
        print(async_result, '--------->', time.clock() - t)
        
        v = c.streaming_range(10, 100, 10)
        for i in v:
            print(i)
            
#         try:
#             c.bad()
#         except Exception, e:
#             print('An error occurred: %s' % e)
    
def server():
    s = zerorpc.Server(CommonModuleServer())
    s.bind('tcp://0.0.0.0:4242')
    s.run()
    
if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], 'ht:')
    t = ''
    for op, v in opts:
        if op == '-t':
            t = v

    if t == 's':
        server()
    elif t == 'c':
        client()