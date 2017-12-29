# -*- coding: UTF-8 -*-

'''
Created on 2017年12月21日

@author: Administrator
'''

import os
import random
import signal
import subprocess
from tornado.ioloop import IOLoop
import tornado.web
import tornado.websocket
import User

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('Hello, world')
    
    def post(self):
        self.write('Hello, world')

class AddHandler(tornado.web.RequestHandler):

    def get(self):
        a = self.request.arguments['a']
        b = self.request.arguments['b']
        li0 = a[0]
        li1 = b[0]
        print(li0.decode())
        print(li1.decode())
        self.write(str(int(li0) + int(li1)))

    def post(self):
        self.write('post')


class Sessions(object):
    ''' 处理类 '''
    
    user_register = []

    def register(self, sender):
        ''' 记录客户端连接实例 '''
        self.user_register.append(sender)

    def unregister(self, sender):
        ''' 删除客户端连接实例 '''
        self.user_register.remove(sender)


class ChatHandler(tornado.websocket.WebSocketHandler):
    ''' 接受websocket链接，保存链接实例 '''

    def check_origin(self, origin):  # 针对websocket处理类重写同源检查的方法
        return True 
            
    def open(self):
        name = self.request.arguments['name']
        upsd = self.request.arguments['upsd']
        rid = self.request.arguments['rid']
        uid = self.request.arguments['uid']
        extra = self.request.arguments['extra']
        
        str_name = name[0].decode()
        str_upsd = upsd[0].decode()
        str_rid = rid[0].decode()
        str_uid = uid[0].decode()
        str_extra = extra[0].decode()
    
        print(str_name)
        print(str_upsd)
        print(str_rid)
        print(str_uid)
        print(str_extra)
        
        Sessions().register(self)
        User.User(self.request.arguments).register()
        
        self.write_message('connected.')

    def on_close(self):
        Sessions().unregister(self)  # 删除客户端连接

    def on_message(self, message):
        print(message)
        self.write_message('22222222222222222222222')


class Application(tornado.web.Application):

    def __init__(self):

        self.handlers = ([
            (r'/', MainHandler),
            (r'/add', AddHandler),
            (r'/ws', ChatHandler),
        ])

        self.settings = dict(
            cookie_secret="1111111111111111111111111111111111",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
        
        tornado.web.Application.__init__(self, self.handlers, **self.settings)


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/add', AddHandler),
        (r'/ws', ChatHandler),
    ])
    
def handle_sigchld(sig, frame):
    IOLoop.current().add_callback_from_signal(IOLoop.current().stop)
    
def main():
    signal.signal(signal.SIGINT, handle_sigchld)
  #     app = make_app()
    app = Application()
    app.listen(8888)
    IOLoop.current().start()


if __name__ == '__main__':
    main()
