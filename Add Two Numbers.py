#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        c=0
        r=0
        lst1 = []
        lst2 = []
        nlst = []
        while l1:
            lst1.append(l1.val)
            l1 = l1.next
        while l2:
            lst2.append(l2.val)
            l2 = l2.next
        len1 = len(lst1)
        len2 = len(lst2)
        if len1>=len2:
            for i in range(len2):
                nlst.append((lst1[i]+lst2[i]+c)%10)
                c = (lst1[i]+lst2[i]+c)/10
            for i in range(len1-len2):
                nlst.append((lst1[len2+i]+c)%10)
                c = (lst1[len2+i]+c)/10
            if c !=0:
                nlst.append(1)
        else:
            for i in range(len1):
                nlst.append((lst1[i]+lst2[i]+c)%10)
                c = (lst1[i]+lst2[i]+c)/10
            for i in range(len2-len1):
                nlst.append((lst2[len1+i]+c)%10)
                c = (lst2[len1+i]+c)/10
            if c !=0:
                nlst.append(1)

        head = ListNode(nlst[0])
        temp = head
        for i in range(len(nlst)-1):
            temp.next = ListNode(nlst[i+1])
            temp = temp.next
        return head