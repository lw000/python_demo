'''
Created on 2018年1月4日

@author: Administrator
'''
import tornado.web


class AddHandler(tornado.web.RequestHandler):
    def get(self):
        a = self.request.arguments['a'][0].decode()
        b = self.request.arguments['b'][0].decode()
        c = self.__add(a, b)
        self.write(str(c))

    def post(self):
        a = self.request.body_arguments['a'][0].decode()
        b = self.request.body_arguments['b'][0].decode()
        c = self.__add(a, b)
        self.write(str(c))

    def __add(self, a, b):
        return int(a) + int(b)


class SubHandler(tornado.web.RequestHandler):
    def get(self):
        a = self.request.arguments['a'][0].decode()
        b = self.request.arguments['b'][0].decode()
        c = self.__sub(a, b)
        self.write(str(c))

    def post(self):
        a = self.request.body_arguments['a'][0].decode()
        b = self.request.body_arguments['b'][0].decode()
        c = self.__sub(a, b)
        self.write(str(c))

    def __sub(self, a, b):
        return int(a) - int(b)


class MulHandler(tornado.web.RequestHandler):
    def get(self):
        a = self.request.arguments['a'][0].decode()
        b = self.request.arguments['b'][0].decode()
        c = self.__mul(a, b)
        self.write(str(c))

    def post(self):
        a = self.request.body_arguments['a'][0].decode()
        b = self.request.body_arguments['b'][0].decode()
        c = self.__mul(a, b)
        self.write(str(c))

    def __mul(self, a, b):
        return int(a) * int(b)
