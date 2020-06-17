# -*- coding:utf-8 -*-
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
for i in range(100):
    msg = '%s:%s'% (i,message)
    channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=msg)
print(" [x] Sent %r" % message)
connection.close()