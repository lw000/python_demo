'''
Created on 2018年1月3日

@author: Administrator
'''

import redis

class RedisHelper(object):
    def __init__(self):
        self.__pool = redis.ConnectionPool(host='192.168.204.128', port=6379)
        self.__conn = redis.Redis(connection_pool=self.__pool)
        self.channel = 'monitor_main'  # 定义名称

    def publish(self, msg):  # 定义发布方法
        self.__conn.publish(self.channel, msg)
        return True

    def subscribe(self):  # 定义订阅方法
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub

    def publish_channel(self, channel, msg):  # 定义发布方法
        self.__conn.publish(channel, msg)
        return True

    def subscribe_channel(self, channel):  # 定义订阅方法
        pub = self.__conn.pubsub()
        pub.subscribe(channel)
        pub.parse_response()
        return pub