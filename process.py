# -*- coding: utf-8 -*-

class Process(object):
	
	def __init__(self,attri):
		
		self.attri = attri	#把生物的属性字典传过来
	
	def attack(self):
		
		kill = -(self.attri[u'力量'] )	#该生物属性下造成的伤害
		
		return kill
		
	def manadestory(self):

		destory = -(self.attri[u"法力值"] )
		
		return destory
	
		
		