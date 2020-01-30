# -*- coding: utf-8 -*-

from random import randint

class Process(object):
	
	def __init__(self,attri):
		
		self.attri = attri	#把生物的属性字典传过来
	
	def attack(self):
		
		kill = -(self.attri[u'力量'] )	#该生物属性下造成的伤害
		
		return kill
		
	def manadestory(self):

		destory = -(self.attri[u"法力值"] )
		
		return destory
	
	def define(self):
	
		armor  = self.attri[u'血量']/4 + self.attri[u'力量']/5 + self.attri[u'法力值']/6
		
		return armor
		
	def run(self):
	
		self.attri[u'金币']  = self.attri[u'金币']*0.6
	
		dice = randint(1,10)
		
		if dice == 1 or dice == 5 :
		
			final = "success"
			
		else:
		
			final = "fail"
			
		return final
		