#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a string
    def convert(self, s, nRows):
        len_str = len(s)
        if len_str<=2 or nRows == 1:
            return s
        step = 2*nRows-2
        result = ""
        for i in range(nRows):
            for j in range(i, len_str, step):
                result += s[j]
                if i > 0 and i < nRows - 1 and j + step - 2 * i < len_str:
                    result += s[j + step - 2 * i]
        return result

