# -*- coding: UTF-8 -*-

'''
Created on 2017年12月21日

@author: Administrator
'''

import os
import sys
import getopt
import signal
from tornado.ioloop import IOLoop
# import tornado.options
import tornado.web

from web_main_handler import MainHandler
from web_calc_handler import AddHandler
from web_calc_handler import SubHandler
from web_calc_handler import MulHandler
from ws_chat_handler import ChatSocketHandler

sys.path.append('./common')
        
class Application(tornado.web.Application):

    def __init__(self):

        self.handlers = ([
            (r'/', MainHandler),
            (r'/add', AddHandler),
            (r'/sub', SubHandler),
            (r'/mul', MulHandler),
            (r'/ws', ChatSocketHandler),
        ])

        self.settings = dict(
            cookie_secret='C7B1AFCC-810E-46d0-8157-09FC488D4C71',
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            #             xsrf_cookies=True,
        )
#         tornado.web.Application.__init__(self, self.handlers, **self.settings)
        super(Application, self).__init__(self.handlers, **self.settings)

def makeApp():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/add', AddHandler),
        (r'/sub', SubHandler),
        (r'/mul', MulHandler),
        (r'/ws', ChatSocketHandler),
    ])

def handle_sigchld(sig, frame):
    IOLoop.current().add_callback_from_signal(IOLoop.current().stop)

def main():
#     tornado.options.parse_command_line()
    
    opts, _ = getopt.getopt(sys.argv[1:], 'ht:')
    t = ''
    for op, v in opts:
        if op == '-t':
            t = v

    if t == 's':
        signal.signal(signal.SIGINT, handle_sigchld)

#         app = makeApp()

        app = Application()
        app.listen(8888)
        IOLoop.current().start()
    elif t == 'c':
        import client
        client.run_client()


if __name__ == '__main__':
    main()
