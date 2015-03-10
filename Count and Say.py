#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a string
    def countAndSay(self, n):
        k = '1'
        for i in xrange(n-1):
            new_k = ''
            j = 0
            while j < len(k):
                cnt = 1
                while j < len(k)-1 and k[j]==k[j+1]:
                    cnt = cnt + 1
                    j = j + 1
                new_k = new_k + '{}{}'.format(cnt,k[j])
                j = j + 1
            k = new_k
        return k
