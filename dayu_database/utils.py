#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

import os
import time

TIME_EPOCH = time.mktime(time.strptime('2010-01-01 00:00:00',
                                       '%Y-%m-%d %H:%M:%S'))


def snowflake():
    '''
    类似twitter 的snowflake 生成函数。
    生成的64 bit 整数，具备全局唯一、自增、分布式的特点。可以保证从2010年开始的79年内 不会生成相同的ID
    :return: 64 bit 整数
    '''
    import uuid
    import random

    user_bit = uuid.getnode() % 16
    pid_bit = os.getpid() % 16
    time_bit = int((time.time() - TIME_EPOCH) * 1000.0)
    guid = ((time_bit << 22) |
            (user_bit << 18) |
            (pid_bit << 14) |
            (random.randint(0, 8191)))
    return guid
