#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def maxArea(self, height):
        left,right = 0, len(height) - 1
        maxV = 0
        while left < right:
            maxV = max(maxV, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxV