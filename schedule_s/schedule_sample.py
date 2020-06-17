# -*- coding:utf-8 -*-
__author__ = 'aihua.sun'

import datetime
import schedule
import threading
import time


def job1():
    print("I'm working for job1")
    time.sleep(2)
    print("job1:",time.ctime(time.time()))


def job2():
    print("I'm working for job2")
    time.sleep(2)
    print("job2:", time.ctime(time.time()))


def job1_task():
    threading.Thread(target=job1).start()


def job2_task():
    threading.Thread(target=job2).start()


def run():
    # 开了一条线程，就把job独立出去运行了，不会占主进程的cpu时间，schedule并没有花掉执行一个任务的时间，
    # 它的开销只是开启一条线程的时间，所以，通过该方法可以保证每次任务的间隔都是5s。
    schedule.every(5).seconds.do(job1_task)
    schedule.every(5).seconds.do(job2_task)

    while True:
        schedule.run_pending()
        time.sleep(1)

run()