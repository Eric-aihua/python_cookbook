# -*- coding:utf-8 -*-
import pika
import faker

from rabbitmq.routing import LogLevelProvider

f = faker.Faker()
f.add_provider(LogLevelProvider)


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')
# 发送100个随机级别以及内容的log
for i in range(10000):
    severity = f.log_level()
    message = f.text()
    channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
    print(" [x] Sent %r:%r" % (severity, message))
connection.close()