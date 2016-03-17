# coding=utf-8

__author__ = 'sinlov'

import re

code_1 = '--------------\n'
code_11 = '---\n'
code_2 = '#dadad'
code_3 = '00:12:12 --> 00:12:14'
code_4 = '12351454'
code_5 = '\n'
code_6 = r'abc fsind me you are funny'

reg_code_1 = r'--------------'
reg_code_2 = r'/A/d*[/n]/Z'
reg_code_3 = r'/d --> /d'
reg_return = r'\n'
reg_find = r'find'

if re.match(reg_find, code_6):
    print 'yes'
else:
    print 'no'

print code_6.find(reg_find)
