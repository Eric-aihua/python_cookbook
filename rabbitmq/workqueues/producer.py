# -*- coding:utf-8 -*-
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)  # make message persistent by durable parameters

message = ' '.join(sys.argv[1:]) or "Hello World!"
for i in range(100):
    msg = '%s:%s' % (i, message)
    channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=msg,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()
