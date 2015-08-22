# coding:utf-8
__author__ = 'sinlov'

import time
import datetime

def default():
    return time.strftime("%Y-%m-%d %H:%M:%S  %s")
def microsecond():
    return int(datetime.datetime.now().microsecond)
