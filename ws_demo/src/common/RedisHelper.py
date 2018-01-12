'''
Created on 2018年1月3日

@author: Administrator
'''

import redis


class RedisHelper(object):
    def __init__(self, host='127.0.0.1', port=6379):
        self.__pool = redis.ConnectionPool(host=host, port=port)
        self.__conn = redis.Redis(connection_pool=self.__pool)
        self.channel = 'monitor_main'  # 定义名称

    def publish(self, msg):  # 定义发布方法
        v = self.__conn.publish(self.channel, msg)
        return v

    def subscribe(self):  # 定义订阅方法
        p = self.__conn.pubsub()
        p.subscribe(self.channel)
        p.parse_response()
        return p

    def publish_channel(self, channel, msg):  # 定义发布方法
        v = self.__conn.publish(channel, msg)
        return v

    def subscribe_channel(self, channel):  # 定义订阅方法
        p = self.__conn.pubsub()
        p.subscribe(channel)
        p.parse_response()
        return p
