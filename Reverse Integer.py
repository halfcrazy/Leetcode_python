#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def reverse(self, x):
        flag = True
        if x < 0:
            flag = False
            x = -x
        x = int(str(x)[::-1])
        if flag == False:
            x = -x
        if x < 2**31 and x > -2**31:
            return x
        return 0