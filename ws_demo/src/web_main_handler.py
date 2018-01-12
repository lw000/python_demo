'''
Created on 2018年1月4日

@author: Administrator
'''
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('{\'code\':0, \'what\':\'Hello, world.\'}')

    def post(self):
        self.write('{\'code\':0, \'what\':\'Hello, world.\'}')