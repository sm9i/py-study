#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module'

__author__ = 'sm9i'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello,world!')
    elif len(args) == 2:
        print('Hello,%s' % args[1])
    else:
        print('Too many arguments!')


# 一般用来运行测试判断模块name
if __name__ == '__main__':
    test()

# private 定义为_
