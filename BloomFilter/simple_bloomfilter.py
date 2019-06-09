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
from bitarray import bitarray


class BloomFilter(object):
    def __init__(self, bit_size=10000, hash_count=3, start_seed=41):
        self.bit_size = bit_size
        self.hash_count = hash_count
        self.start_seed = start_seed
        self.initialize()

    def initialize(self):
        self.bit_array = bitarray(self.bit_size)
        self.bit_array.setall(0)

    def add(self, data):
        bit_points = self.get_hash_points(data)
        for index in bit_points:
            self.bit_array[index] = 1

    def is_contain(self, data):
        bit_points = self.get_hash_points(data)
        result = [self.bit_array[index] for index in bit_points]
        return all(result)

    def get_hash_points(self, data):
        return [
            mmh3.hash(data, index) % self.bit_size
            for index in range(self.start_seed, self.start_seed +
                               self.hash_count)
        ]


if __name__ == '__main__':
    bloomFilter = BloomFilter()
    bloomFilter.add('hello')
    print(bloomFilter.is_contain('hello'))
    print(bloomFilter.is_contain('hello_world'))
