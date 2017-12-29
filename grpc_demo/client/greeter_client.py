'''
Created on 2017年12月28日

@author: Administrator
'''

import grpc

import time
import sys
from concurrent import futures

sys.path.append('./')
sys.path.append('../')
sys.path.append('../proto')

import chat_pb2
import chat_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50052')
    stub = chat_pb2_grpc.GreeterStub(channel)
    for i in range(1000):
        t = time.time()
        reponse = stub.SayHello(chat_pb2.HelloRequest(name='liwei'))
        t1 = time.time()-t
        print(reponse, t1)
    
if __name__ == '__main__':
    run()