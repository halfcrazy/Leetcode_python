#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        cnt = 0
        for i in xrange(length-1):
            if A[i]==A[i+1]:
                length = length - 1
                cnt = cnt + 1
            else :
                A[i+1-cnt]=A[i+1]
        return length
