# -*- coding: UTF-8 -*-

'''
Created on 2017年12月21日

@author: Administrator
'''

from __future__ import print_function

import os
import geventwebsocket

from geventwebsocket.server import WebSocketServer


def echo_app(environ, start_response):
    websocket = environ.get('wsgi.websocket')

    if websocket is None:
        return http_handler(environ, start_response)
    try:
        while True:
            message = websocket.receive()
            websocket.send(message)
        websocket.close()
    except geventwebsocket.WebSocketError as ex:
        print('{0}: {1}'.format(ex.__class__.__name__, ex))


def http_handler(environ, start_response):
    if environ['PATH_INFO'].strip('/') == 'version':
        start_response('200 OK', [])
        return [agent]

    else:
        start_response('400 Bad Request', [])

        return ['WebSocket connection is expected here.']


if __name__ == '__main__':
    path = os.path.dirname(geventwebsocket.__file__)
    agent = bytearray('gevent-websocket/%s' % (geventwebsocket.get_version()),
                      'latin-1')
    print('Running %s from %s' % (agent, path))
    ser = WebSocketServer(('', 8000), echo_app, debug=False)
    ser.serve_forever()
