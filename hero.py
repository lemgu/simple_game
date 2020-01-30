# -*- coding: utf-8 -*-



import attribute

class Hero_random(object):

	def attribute(self): 
	
		attri = attribute.Attribute_random(0).attri()
		
		return attri
		
class Hero_average(object):
	
	def attribute(self): 
	
		attri = attribute.Attribute_given(5,3,2,0,0).attri()	#血量、法力值、力量、金币
	
		return attri
		
class Hero_king(object):

	def attribute(self): 
	
		attri = attribute.Attribute_given(10,0,5,100,0).attri()
		
		return attri
		
		
