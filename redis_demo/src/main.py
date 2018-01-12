'''
Created on 2018年1月3日

@author: Administrator
'''

import _thread
import threading
import time
import json
import queue
import logging
from RedisHelper import RedisHelper
from MySqlHelper import MysqlHelper
from flask import Flask
from flask import request
from flask import render_template
from _multiprocessing import recv

# from flask import sessions

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s %(filename)s[line:%(lineno)d]',
                    datefmt='%a, %d %b %Y %H:%M:%S')

app = Flask(__name__)
redis = RedisHelper()
mysql = MysqlHelper()
task_queue = queue.Queue()


class RecvedServer(threading.Thread):
    def __init__(self, q, name):
        self.__quit = False
        self.__q = q
        super(RecvedServer, self).__init__(name=name)

    def quitWorker(self):
        self.__quit = True

    def run(self):
        redis_sub = redis.subscribe_channel('/liwei/000')  # 调用订阅方法
        while True:
            msg = redis_sub.parse_response()
            self.__q.put(msg)


class Worker(threading.Thread):
    def __init__(self, q, name):
        self.__quit = False
        self.__q = q
        super(Worker, self).__init__(name=name)

    def quitWorker(self):
        self.__quit = True

    def run(self):
        while not self.__quit:
            data = self.__q.get()
            print('%s topic: %s' % (self.name, data[1].decode('utf8')))
            print('%s data: %s' % (self.name, data[2].decode('utf8')))


@app.route('/', methods=['GET', 'POST'])
def home():
    #     return '<h1>Home</h1>'
    return render_template('./home.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.environ["REQUEST_METHOD"] == 'POST':
        a = request.form.get('a')
        b = request.form.get('b')
    elif request.environ["REQUEST_METHOD"] == 'GET':
        a = request.args.get('a')
        b = request.args.get('b')
    else:
        s = json.dumps(
            {'code': '-10', 'what': 'not support method'}, ensure_ascii=False)
        return s
    return str(int(a) + int(b))

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():

    if request.environ["REQUEST_METHOD"] == 'POST':
        task_id = request.form.get('task_id')
        task_start_time = request.form.get('task_start_time')
        task_end_time = request.form.get('task_end_time')
        task_time = request.form.get('task_time')
        task_ext = request.form.get('task_ext')
    elif request.environ["REQUEST_METHOD"] == 'GET':
        task_id = request.args.get('task_id')
        task_start_time = request.args.get('task_start_time')
        task_end_time = request.args.get('task_end_time')
        task_time = request.args.get('task_time')
        task_ext = request.args.get('task_ext')
    else:
        s = json.dumps(
            {'code': '-10', 'what': 'not support method'}, ensure_ascii=False)
        return s

    if not task_id:
        s = json.dumps(
            {'code': '-1', 'what': 'task_id is empty'}, ensure_ascii=False)
        return s

    if not task_start_time:
        s = json.dumps(
            {'code': '-1', 'what': 'task_start_time is empty'}, ensure_ascii=False)
        return s

    if not task_end_time:
        s = json.dumps(
            {'code': '-1', 'what': 'task_end_time is empty'}, ensure_ascii=False)
        return s

    if not task_time:
        s = json.dumps(
            {'code': '-1', 'what': 'task_time is empty'}, ensure_ascii=False)
        return s

    if not task_ext:
        s = json.dumps(
            {'code': '-1', 'what': 'task_ext is empty'}, ensure_ascii=False)
        return s

    res = {'task_id': task_id, 'task_start_time': task_start_time,
           'task_end_time': task_end_time, 'task_time': task_time}
    s = json.dumps(res, ensure_ascii=False)
    redis.publish_channel('/liwei/000', s)  # 发布

    return json.dumps({'code': '0', 'what': 'ok'}, ensure_ascii=False)


def main():
    try:
        #         t = threading.Thread(target=redis_recved_data_server,
        #                              name='redis_recved_data_server', args=('redis_recved_data_server', task_queue))
        #         t.start()

        recver = RecvedServer(task_queue, 'recver')
        recver.start()

        worker = Worker(task_queue, 'worker')
        worker.start()

        app.run(host='127.0.0.1', port=5000)

    except KeyboardInterrupt:
        print('error: unable to start thread')


if __name__ == '__main__':
    main()
