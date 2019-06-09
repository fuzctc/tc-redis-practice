# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-06-09 16:51:45
'''
BEGIN
function:
    RedisBloom Test
END
'''

import redis
client = redis.StrictRedis()

client.delete("tiancheng")
size = 100000
count = 0
client.execute_command("bf.reserve", "tiancheng", 0.001, size)
for i in range(size):
    client.execute_command("bf.add", "tiancheng", "tc%d" % i)
    result = client.execute_command("bf.exists", "tiancheng", "tc%d" % (i + 1))
    if result == 1:
        #print(i)
        count += 1

print("size: {} , error rate: {}%".format(
    size, round(count / size * 100, 5)))
