#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        length = len(num)
        diff = 9999999999999
        result = 0
        for idx, key in enumerate(num[:-2]):
            if idx > 0 and num[idx] == num[idx - 1]:
                continue
            a = num[idx]
            low = idx + 1
            high = length - 1
            while low < high:
                b = num[low]
                c = num[high]
                Sum = a + b + c
                if Sum == target:
                    return target
                else:
                    if abs(Sum - target) < diff:
                        diff = abs(Sum - target)
                        result = Sum
                    if  Sum - target > 0:
                        while high > low and num[high] == num[high - 1]:
                            high -= 1
                        high -= 1
                    else:
                        while low < length - 1 and num[low] == num[low + 1]:
                            low += 1
                        low += 1
        return result
