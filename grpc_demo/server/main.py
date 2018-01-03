'''
Created on 2017年12月28日

@author: Administrator
'''

import os
import grpc
import sys
import getopt
import time
from concurrent import futures
import cProfile

root_path = os.path.dirname(__file__)
sys.path.append('./')
sys.path.append('../')
sys.path.append('../proto')

import chat_pb2
import chat_pb2_grpc

import route_database_pb2
import route_database_pb2_grpc

import route_db

_ONE_DAY_IN_SECONDS = 60 * 1

class Calc(chat_pb2_grpc.CalcServicer):
    
    def add(self, request, context):
        return chat_pb2.Result(c = request.a + request.b);
    
    def sub(self, request, context):
        return chat_pb2.Result(c = request.a - request.b);
    
    def mul(self, request, context):
        return chat_pb2.Result(c = request.a * request.b);

class Greeter(chat_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return chat_pb2.HelloReply(message='Hello, %s!' % request.name)
    

class Route(route_database_pb2_grpc.RouteGreeterServicer):
    
    def __init__(self):
        #     db = cProfile.run('route_db.read_route_database()')
        self.db = route_db.read_route_database()
        print(self.db)
        
    def GetFeature(self, request, context):
        for feature in self.db:
            if feature.location == request:
                return feature
        return None
    
    def ListFeatures(self, request, context):
        pass
    
    def RecordRoute(self, request, context):
        pass
    
    def RouteChat(self, request, context):
        pass
    
    
def client_Greeter():
    channel = grpc.insecure_channel('localhost:50052')
    stub = chat_pb2_grpc.GreeterStub(channel)
#     routestub = route_database_pb2_grpc.RouteGreeterStub(channel)
    calcstub = chat_pb2_grpc.CalcStub(channel)
    
    for i in range(100):
        t = time.time()
        reponse = stub.SayHello(chat_pb2.HelloRequest(name='liwei'))
        print(i, ' >>>>>>>>', reponse, time.time() - t)
        
#     for _ in range(10):
#         t = time.time()
#         reponse = routestub.GetFeature(route_database_pb2.FeatureRequest(route_database_pb2.Point(latitude=408122808, longitude=743999179)))
#         t1 = time.time() - t
#         print(i, ' >>>>>>>>', reponse, t1)
        
    for i in range(100):
        t = time.time()
        reponse = calcstub.add(chat_pb2.Value(a=10, b=20))
        print(i, ' >>>>>>>>', reponse, time.time() - t)
        
        t = time.time()
        reponse = calcstub.sub(chat_pb2.Value(a=10, b=20))
        print(i, ' >>>>>>>>', reponse, time.time() - t)
        
        t = time.time()
        reponse = calcstub.mul(chat_pb2.Value(a=10, b=20))
        print(i, ' >>>>>>>>', reponse, time.time() - t)

def server():
     
    srv = grpc.server(futures.ThreadPoolExecutor(max_workers=(10)))
    chat_pb2_grpc.add_GreeterServicer_to_server(Greeter(), srv)
    chat_pb2_grpc.add_CalcServicer_to_server(Calc(), srv)
#     route_database_pb2_grpc.add_RouteGreeterServicer_to_server(Route(), srv)
    srv.add_insecure_port('[::]:50052')
    srv.start()

    try:
        while True:
            print('looping')
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        srv.stop(0)

def main():
    opts, _ = getopt.getopt(sys.argv[1:], 'ht:')
    t = ''
    for op, v in opts:
        if op == '-t':
            t = v

    if t == 's':
        server()
    elif t == 'c':
        client_Greeter()


if __name__ == '__main__':
    main()
