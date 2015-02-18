#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def romanToInt(self, s):
        num = 0
        length = len(s)
        pair = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for idx, letter in enumerate(s[:-1]):
            if pair[letter] >= pair[s[idx + 1]]:
                num += pair[letter]
            else:
                num -= pair[letter]
        num += pair[s[-1]]
        return num
