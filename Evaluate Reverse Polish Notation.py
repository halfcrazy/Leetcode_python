#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
	def suan(self,lop,rop,op):
		if op=="+":
			rst=lop+rop
		elif op=="-":
			rst=lop-rop
		elif op=="*":
			rst=lop*rop
		elif op=="/":
			rst=int(float(lop)/rop)
		return rst
	# @param tokens, a list of string
	# @return an integer
	def evalRPN(self, tokens):
		stack=[]
		for op in tokens:
			if op=="+" or op=="-" or op=="*" or op=="/":
				rop=stack.pop()
				lop=stack.pop()
				rst=self.suan(lop,rop,op)
				print lop,op,rop
				stack.append(rst)
			else:
				num=int(op)
				stack.append(num)
			result=stack[0]
			
		return result
