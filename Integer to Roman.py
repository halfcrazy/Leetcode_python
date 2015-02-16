#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a string
    def intToRoman(self, num):
        result = ""
        pair = [('I',1),('IV',4),('V',5),('IX',9),('X',10),('XL',40),('L',50),('XC',90),('C',100),('CD',400),('D',500),('CM',900),('M',1000)]
        for symbol, number in reversed(pair):
            while num >= number:
                num -= number
                result += symbol
        return result