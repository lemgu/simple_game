# -*- coding: utf-8 -*-

from random import randint

class Attribute_random(object):

	def __init__(self,camp):

		self.blood = randint(1,11)
		self.mana = randint(1,11)	#mana，意为法力值
		self.strength = randint(1,11)
		self.money = randint(50,100)	#随机赋予生物初始化的属性值
		self.camp = camp	#camp 阵营，用于标识是英雄还是对方的属性值。camp为0时为英雄属性，1时为对方属性
	
	def attri(self): 
		
		create_attri = {u"血量":self.blood,u"法力值":self.mana,u"力量":self.strength,u"金币":self.money,u"阵营":self.camp}
		
		return create_attri
		
class Attribute_given(object):
	
	def __init__(self,blood,mana,strength,money,camp):

		self.blood = blood
		self.mana = mana	
		self.strength = strength
		self.money = money	
		self.camp = camp
	
	def attri(self):
		
		create_attri = {u"血量":self.blood,u"法力值":self.mana,u"力量":self.strength,u"金币":self.money,u"阵营":self.camp}
		
		return create_attri
		
