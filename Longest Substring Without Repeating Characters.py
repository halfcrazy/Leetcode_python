#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLongestSubstring(self,s):
        if len(s)<2:
            return len(s)
        idx = -1
        max_len = 0
        table = {}
        for i in range(256):
            table[chr(i)] = -1

        for i,v in enumerate(s):
            if table[v] > idx:
                idx = table[v]
            if i - idx > max_len:
                max_len = i - idx
            table[v] = i
        return max_len
