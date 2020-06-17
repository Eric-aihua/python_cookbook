# -*- coding:utf-8 -*-
import subprocess


def exec_by_subprocess_call():
    try:
        ret = subprocess.call('ping www.baidu.com')
        # ret = subprocess.call('cd d://')
        print ret
    except BaseException, ex:
        print '>>>>>>error:%s' % ex


def exec_by_subprocess_check_call():
    try:
        # ret = subprocess.check_call('cd d:/')
        ret = subprocess.check_call('ping www.baidu.com')
        print ret
    except BaseException, ex:
        print '>>>>>>error:%s' % ex

exec_by_subprocess_call()
# exec_by_subprocess_check_call()
