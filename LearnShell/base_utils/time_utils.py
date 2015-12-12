# coding:utf-8
__author__ = 'sinlov'

import time
import datetime


def default():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def microsecond():
    return int(datetime.datetime.now().microsecond)


def str_format():
    result = [str(time.strftime("%Y-%m-%d %H:%M:%S")), " .", str(microsecond())]
    return "".join(result)
