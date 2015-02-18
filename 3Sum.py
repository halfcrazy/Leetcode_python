#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        result = set()
        num.sort()
        for idx1, key1 in enumerate(num):
            for idx2, key2 in enumerate(num[idx1 + 1:]):
                if (0 - key1 - key2) in num[idx1 + idx2 + 2:]:
                    result.add(tuple([key1, key2, 0 - key1 - key2]))
        return [list(i) for i in result]