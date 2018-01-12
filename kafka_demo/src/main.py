'''
Created on 2018年1月8日

@author: Administrator
'''
from pykafka import KafkaClient
import codecs
import logging

logging.basicConfig(level = logging.INFO)

client = KafkaClient(hosts = "172.16.82.163:9091")

#生产kafka数据，通过字符串形式
def produce_kafka_data(kafka_topic):
    with kafka_topic.get_sync_producer() as producer:
        for i in range(4):
            producer.produce('test message' + str(i ** 2))

#消费kafka数据
def consume_simple_kafka(kafka_topic, timeout):
    consumer = kafka_topic.get_simple_consumer(consumer_timeout_ms = timeout)
    for message in consumer:
        if message is not None:
            print(message.offset, message.value)

if __name__ == '__main__':
    pass