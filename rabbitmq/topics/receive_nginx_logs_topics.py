# -*- coding:utf-8 -*-
import pika
import sys
"""搜集ngnix的所有日志"""

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# 搜集ngnix的所有日志
severities = 'nginx.*.*'

channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=severities)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()