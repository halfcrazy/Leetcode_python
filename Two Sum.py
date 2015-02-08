#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        nlst = sorted(num)
        i1=0
        i2=0
        for k in nlst:
            for j in nlst[nlst.index(k)+1:]:
                if k+j > target:
                    break
                elif k+j == target:
                    i1=num.index(k)+1
                    i2=num.index(j)+1
                    if i1==i2:
                        i2=num.index(j,i1)+1
                    if i1>i2:
                        i1,i2=i2,i1
                    return (i1,i2)
                else:
                    continue