'''
Created on 2017年12月28日

@author: Administrator
'''
import zerorpc
import time

if __name__ == '__main__':
    c = zerorpc.Client()
    c.connect("tcp://127.0.0.1:4242")

    for i in range(10):
        t = time.time()
        print(c.hello("RPC"))
        t1 = time.time() - t
        print(t1)
        t = time.time()
        print(c.add(1, 2))
        t1 = time.time() - t
        print(t1)
        t = time.time()
        print(c.len('aaaaaaaaaaaaa'))
        t1 = time.time() - t
