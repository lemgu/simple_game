# -*- coding: utf-8 -*-

class a(object):
	
	def __init__(self):
	
		pass
		
	def change(self,a,b):
	
		c = a + b
		
		return c,114514
		
test = a().change(10,5)

print test

s,b = test
print s
print b

