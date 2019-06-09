# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-06-09 19:49:53
'''
BEGIN
function:
    pyreBloom Test
END
'''
from pyreBloom import pyreBloom


def convert_utf8(data):
    """
    convert utf8
    """
    if isinstance(data, str):
        return data.encode('utf8')
    elif isinstance(data, tuple):
        data = tuple([convert_utf8(item) for item in data])
    elif isinstance(data, list):
        for idx, i in enumerate(data):
            data[idx] = convert_utf8(i)
    elif isinstance(data, dict):
        for i in data:
            data[i] = convert_utf8(data[i])
    return data


redis_conf = {'host': '127.0.0.1', 'password': '', 'port': 6379, 'db': 0}

for k, v in redis_conf.items():
    redis_conf = convert_utf8(redis_conf)

key = convert_utf8('tc')
value = convert_utf8('hello')

p = pyreBloom(key, 10000, 0.001, **redis_conf)
p.add(value)
print(p.contains(value))
