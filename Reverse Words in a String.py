#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s=s.strip()
        if s=="":
            return ""
        else:
			s=s.split(" ")
			s=[x for x in s if x!=""]
			return " ".join(s[::-1])