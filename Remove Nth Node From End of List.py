#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head.next is None:
            return None
        p1 = head
        p2 = head
        for i in xrange(n-1):
            if p1.next is None:
                break
            p1 = p1.next
        if p1.next is None:
            return p2.next
        else:
            while p1.next.next is not None:
                p1 = p1.next
                p2 = p2.next
            p2.next = p2.next.next
            return head
