#!/usr/bin/python3

# -*- coding:utf-8 -*-
# @Time     : 2019/9/7 16:10
# @Author   : Aaron Ran
# @Email    : aaronran07@outlook.com
# @File     : utils.py
# @Software : PyCharm


import cProfile
import pstats

def profile(func):
    """
    a decorator that uses cProfile to profile a function.

    :param func: the function name which will be profiled
    :return:
    """

    def inner(*arg, **kwargs):
        pf = cProfile.Profile()
        pf.enable()
        retval = func(*arg, **kwargs)
        pf.disable()

        s = open('./profile_log.txt', 'a+')
        sortby = 'cumulative'
        ps = pstats.Stats(pf, stream=s).sort_stats(sortby)
        ps.print_stats()  # print the first 10% of the list.
        return retval

    return inner
