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

_ONE_DAY_IN_SECONDS = 60*1

class Greeter(chat_pb2_grpc.GreeterServicer):
    
    def SayHello(self, request, context):   
        return chat_pb2.HelloReply(message='Hello, %s!' % request.name)
       
def main():
    serv = grpc.server(futures.ThreadPoolExecutor(max_workers=(10)))
    chat_pb2_grpc.add_GreeterServicer_to_server(Greeter(), serv)
    serv.add_insecure_port('[::]:50052')
    serv.start()
    
    try:
        while True:
            print('looping')
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        serv.stop(0)
     
if __name__ == '__main__':
    main()