# -*- coding:utf-8 -*-
import random

import pika
import faker
from faker.providers import BaseProvider
"""发射包括有服务器，系统，日志级别组合的日志，格式为  服务器.系统.日志级别"""

class LogLevelProvider(BaseProvider):
    def log_level(self):
        log_level_list = 'debug,info,warn,error'.split(',')
        return random.choice(log_level_list)

class ServerProvider(BaseProvider):
    def server(self):
        log_level_list = 'nginx,tomcat,uwsgi,jersy'.split(',')
        return random.choice(log_level_list)

class SystemProvider(BaseProvider):
    def system(self):
        log_level_list = 'CMS,Content,Sales'.split(',')
        return random.choice(log_level_list)

f = faker.Faker()
f.add_provider(LogLevelProvider)
f.add_provider(ServerProvider)
f.add_provider(SystemProvider)


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')
# 发送100个随机级别以及内容的log
for i in range(100):
    severity = '%s.%s.%s'% (f.server(),f.system(),f.log_level())
    message = f.text()
    msg = '%s:%s' % (i, message)
    channel.basic_publish(exchange='topic_logs',
                      routing_key=severity,
                      body=msg)
    print(" [x] Sent %r:%r" % (severity, message))
connection.close()