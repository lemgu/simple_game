# -*- coding: utf-8 -*-

class a(object):
	
	def __init__(self,dict):
	
		self.dict = dict
		
	def change(self):
	
		self.dict = [0,1,2,3]
		
		return self.dict
		
dic = [51,23,13,8]

test = a(dic).change()

print dic

print test