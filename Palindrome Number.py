#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        length = 0
        tmp = x
        while tmp > 0:
            tmp /= 10
            length += 1
        for i in xrange(length/2):
            tmp1 = x #记录最低位
            tmp2 = x #记录最高位
            tmp1 /= 10**i
            tmp1 %= 10
            tmp2 /= 10**(length - i - 1)
            if tmp2 >= 10:
                tmp2 %= 10
            if tmp1 != tmp2:
                return False
        return True