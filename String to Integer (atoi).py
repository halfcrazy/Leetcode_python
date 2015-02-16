#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def atoi(self, str):
        import re
        pattern = re.compile("^([-+]?\d+)")
        preparse = str.strip()
        try:
            number_str = pattern.search(preparse).groups()[0]
        except:
            return 0
        num = int(number_str)
        if num < 2**31 and num >= -2**31:
            return num
        if num >= 2**31:
            return 2**31-1
        if num < -2**31:
            return -2**31