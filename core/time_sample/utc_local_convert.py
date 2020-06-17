# -*- coding:utf-8 -*-
# @Author：sunaihua

import time
import datetime
import pytz


def utc2local(utc_st):
    'UTC时间转本地时间（+8:00）'
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st

def local2utc(local_st):
    '本地时间转UTC时间（-8:00）'
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.datetime.utcfromtimestamp(time_struct)
    return utc_st

# UTCS时间转换为时间戳 2016-07-31T16:00:00Z
def utc_to_local(utc_time_str, utc_format='%Y-%m-%dT%H:%M:%SZ'):
    local_tz = pytz.timezone('Asia/Chongqing')
    local_format = "%Y-%m-%d %H:%M"
    utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    time_str = local_dt.strftime(local_format)
    return int(time.mktime(time.strptime(time_str, local_format)))
 
# 本地时间转换为UTC
 
def local_to_utc(local_ts, utc_format='%Y-%m-%dT%H:%MZ'):
    local_tz = pytz.timezone('Asia/Chongqing')
    local_format = "%Y-%m-%d %H:%M"
    time_str = time.strftime(local_format, time.localtime(local_ts))
    dt = datetime.datetime.strptime(time_str, local_format)
    local_dt = local_tz.localize(dt, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt.strftime(utc_format)
	
utc_time = datetime.datetime(2014, 9, 18, 10, 42, 16, 126000)

# utc转本地
local_time = utc2local(utc_time)
print local_time.strftime('%Y-%m-%d %H:%M:%S')
# output：2014-09-18 18:42:16


# 本地转utc
utc_tran = local2utc(local_time)
print utc_tran.strftime('%Y-%m-%d %H:%M:%S')
# output：2014-09-18 10:42:16
