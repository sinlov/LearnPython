# coding:utf-8
__author__ = 'sinlov'
from LearnShell.base_utils import time_utils

# test speed
fGt = time_utils.microsecond()
for j in range(10000):
    pass
print(time_utils.default(), time_utils.microsecond() - fGt)
fGt = time_utils.microsecond()
for i in range(100):
    for k in range(100):
        pass
print(time_utils.default(), time_utils.microsecond() - fGt)

print(time_utils.str_format())
