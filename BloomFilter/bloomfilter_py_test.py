# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhichang Fu
# Created Time: 2019-06-09 10:33:48
'''
BEGIN
function:
    Bloom Filter
END
'''

import mmh3
import redis


class BloomFilter(object):
    def __init__(self, bf_key, bit_size=10000, hash_count=3, start_seed=41):
        self.bit_size = bit_size
        self.hash_count = hash_count
        self.start_seed = start_seed
        self.client = redis.StrictRedis()
        self.bf_key = bf_key

    def add(self, data):
        bit_points = self._get_hash_points(data)
        for index in bit_points:
            self.client.setbit(self.bf_key, index, 1)

    def madd(self, m_data):
        if isinstance(m_data, list):
            for data in m_data:
                self.add(data)
        else:
            self.add(m_data)

    def exists(self, data):
        bit_points = self._get_hash_points(data)
        result = [
            self.client.getbit(self.bf_key, index) for index in bit_points
        ]
        return all(result)

    def mexists(self, m_data):
        result = {}
        if isinstance(m_data, list):
            for data in m_data:
                result[data] = self.exists(data)
        else:
            result[m_data] = self.exists[m_data]
        return result

    def _get_hash_points(self, data):
        return [
            mmh3.hash(data, index) % self.bit_size
            for index in range(self.start_seed, self.start_seed +
                               self.hash_count)
        ]


if __name__ == '__main__':
    bloomFilter = BloomFilter("tc")
    bloomFilter.add('hello')
    print(bloomFilter.exists('hello'))
    print(bloomFilter.exists('hello_world'))
