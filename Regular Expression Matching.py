#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        import re
        pattern = re.compile("^" + p + "$")
        if pattern.search(s) is None:
            return False
        return True