# -*- coding: UTF-8 -*-

'''
Created on 2017年12月14日

@author: Administrator
'''

import pika
import _thread
import threading


def send_message():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    while True:
        channel.basic_publish(exchange='', routing_key='hello', body='hello world')
        
    connection.close()

def get_message():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_consume(consumer_callback, queue='hello', no_ack=True)
    
    print('[*] Waiting for message. To exit press CTRL+C')
    
    channel.start_consuming()

def consumer_callback(ch, method, properties, body):
    print('Received %r' % (body))

if __name__ == '__main__':
    t1 = threading.Thread(target=send_message,
                              name='send_message', args=())
    t1.start()
    
    t2 = threading.Thread(target=get_message,
                              name='get_message', args=())
    t2.start()
    
    while True:
        pass
