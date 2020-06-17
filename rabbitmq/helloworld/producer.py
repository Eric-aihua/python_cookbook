# -*- coding:utf-8 -*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello')

for i in range(10):
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World:%s!'% i)
print(" [x] Sent 'Hello World!'")
connection.close()