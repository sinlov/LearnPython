# coding=utf-8
from LearnShell.base_utils import time_utils

__author__ = '"sinlov"'

V = " V "
I = " I "
D = " D "
W = " W "
E = " E "


def v(where, message):
    res = [time_utils.default(), V, "[", where, "] ", message]
    return "".join(res)


def i(where, message):
    res = [time_utils.default(), I, "[", where, "] ", message]
    return "".join(res)


def d(where, message):
    res = [time_utils.default(), D, "[", where, "] ", message]
    return "".join(res)


def w(where, message):
    res = [time_utils.default(), W, "[", where, "] ", message]
    return "".join(res)


def e(where, message):
    res = [time_utils.default(), E, "[", where, "] ", message]
    return "".join(res)
