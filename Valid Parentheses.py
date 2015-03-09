#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        pairs = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in pairs.values():
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if stack.pop() == pairs[i]:
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        return False