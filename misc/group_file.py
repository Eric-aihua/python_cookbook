#coding=utf-8
import os
import sys
import time
import shutil

'''
将手机里的文件自动按照日期分成文件夹
'''

base_dir="/Users/eric/Movies/Videos/WeiXin"

def split_file():
    for i in os.listdir(base_dir):
        if i.endswith(".mp4"):
            month=""
            if i.startswith("VID"):
                month= i[4:10]
            if i.startswith("1"):
                month= time.strftime("%Y%m",time.localtime(float(i[:10])))
            if i.startswith("mmexport"):
                #mmexport1566663147458.jpg
                month=time.strftime("%Y%m",time.localtime(float(i[8:18])))
            if i.startswith("wx_camera"):
                #wx_camera_1544877511524
                month=time.strftime("%Y%m",time.localtime(float(i[len("wx_camera_"):len("wx_camera_")+10])))
            
            if not os.path.exists(os.path.join(base_dir,month)):
                os.mkdir(os.path.join(base_dir,month))
            shutil.copy(os.path.join(base_dir,i),os.path.join(base_dir,month))

split_file()