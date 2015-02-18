#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        max_len = 0
        if strs == [] or "" in strs:
            return ""
        boundary = min(map(len,strs))
        for i in xrange(1,boundary + 1):
            result = [S.startswith(strs[0][:i]) for S in strs]
            if False in result:
                break
            else:
                max_len = i
        return strs[0][:max_len]
