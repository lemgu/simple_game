# -*- coding: utf-8 -*-

import attribute

class Monster_random(object):

	def attribute(self): 
	
		attri = attribute.Attribute_random(1).attri()
		
		
		return attri
		
class Monster_seeker(object):
	
	def attribute(self): 
	
		attri = attribute.Attribute_given(5,3,2,0,1).attri()
		
		return attri
		
class Monster_dragon(object):

	def attribute(self): 
	
		attri = attribute.Attribute_given(10,10,10,10,1).attri()
		
		
		return attri
		
		
