# coding=utf-8

__author__ = 'sinlov'

# Description: parse the argv in python
#
# python test.py xxx -a 1 --b 2 2 4 -t
#
# data: {"default":["xxx"], "-a":["1"], "--b":["2","2","4"], "-t":[]}
#
#
# usage
#
# import cli_argv_parser
# cli_argv_parser.load()
# a = cli_argv_parser.read("-a")       # 1
# b = cli_argv_parser.read("--b")       # 2
# b1 = cli_argv_parser.readList("--b")  # ["2","2","4"]
# c = cli_argv_parser.read()          # xxx
# d = cli_argv_parser.read("--b","-a")   # 2
# e = cli_argv_parser.read("-e")       # None
# t = cli_argv_parser.read("-t")       # ""

import sys

data = {"default": []}


def load():
    if len(sys.argv[1:]) == 0: return False
    key = "default"
    for raw in sys.argv[1:]:
        if raw.startswith("-"):
            key = raw
            if key not in data: data[key] = []
        else:
            data[key].append(raw)
    return True


def read(*args):
    if len(args) == 0: return _getVal("default")
    for key in args:
        if key in data: return _getVal(key)
    return None


def readList(*args):
    if len(args) == 0: return data["default"]
    for key in args:
        if key in data: return data[key]
    return None


def _getVal(key): return data[key][0] if len(data[key]) > 0 else ""

if __name__ == '__main__':
    load()
    a = read("-a")       # 1
    b = read("--b")       # 2
    b1 = readList("--b")  # ["2","2","4"]
    c = read()          # xxx
    d = read("--b","-a")   # 2
    e = read("-e")       # None
    t = read("-t")       # ""

    print a, b, b1, c, d, e, t
