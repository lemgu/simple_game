# -*- coding: utf-8 -*-

from random import randint

class Attribute_random(object):

	def __init__(self):

		self.blood = randint(1,11)
		self.mana = randint(1,11)	#mana，意为法力值
		self.strength = randint(1,11)
		self.money = randint(50,100)	#随机赋予生物初始化的属性值
	
	def attri(self): 
		
		create_attri = {u"血量":self.blood,u"法力值":self.mana,u"力量":self.strength,u"金币":self.money}
		
		return create_attri
		
class Attribute_given(object):
	
	def __init__(self,blood,mana,strength,money):

		self.blood = blood
		self.mana = mana	
		self.strength = strength
		self.money = money	
	
	def attri(self):
		
		create_attri = {u"血量":self.blood,u"法力值":self.mana,u"力量":self.strength,u"金币":self.money}
		
		return create_attri