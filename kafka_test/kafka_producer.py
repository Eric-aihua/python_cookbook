# encoding:utf-8
import time
import random
import string

__author__ = 'aihua.sun'

import logging
from kafka import KafkaProducer
from kafka import KafkaClient

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    # 如果配置filename就会输出到文件，否则就在console
                    # filename='myapp.log',
                    filemode='w')
hosts = "cdh1:9092,cdh2:9092,cdh3:9092"
topic = 'test'


class KafkaSender():

    def __init__(self):
        # self.producer = KafkaProducer(bootstrap_servers=hosts, compression_type='lz4')
        self.producer = KafkaProducer(bootstrap_servers=hosts)
        # self.client.ensure_topic_exists(topic)

    def send_messages(self, msg):
        send_msg=msg*1000
        logging.info(">>>>>>>>>>>>>>>"+str(len(send_msg)/1024))
        self.producer.send(topic, send_msg)
        self.producer.flush()


def get_instance():
    return KafkaSender()


if __name__ == "__main__":
    begin = time.time()
    producer = get_instance()
    for i in range(0, 100):
        msg = 'Message' + str(time.time) + ' ' + ''.join(random.choice(string.lowercase) for i in range(64))
        producer.send_messages(msg)
        time.sleep(0.1)
    end = time.time()
    time.sleep(10)
    print("use time:" + str((end - begin)))
