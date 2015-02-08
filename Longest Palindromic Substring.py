#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def longestPalindrome(self,s):
        if len(s) < 2:
            return s
        longest = ''
        len_s = len(s)
        for idx in range(len(s[:-1])):
            left = idx
            right = idx
            while left>=0 and right<len_s and s[left]==s[right]:
                left-=1
                right+=1
            longest1 = s[left+1:right]
            if len(longest1)>len(longest):
                longest = longest1
            left = idx
            right = idx+1
            while left>=0 and right<len_s and s[left]==s[right]:
                left-=1
                right+=1
            longest2 = s[left+1:right]
            if len(longest2)>len(longest):
                longest = longest2
        return longest
