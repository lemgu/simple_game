# -*- coding: utf-8 -*-

#工具函数

from random import randint
import monster
import inspect	#inspect 模块用于等会用于查找文件中的类

class Utility_function(object):
	
	def choose_monster_random(self):	#随机选取怪物房的怪物
		
		mons = []
		
		all = inspect.getmembers(monster)	#查找monster中的所有模块名
		
		for name,obj in all:	#inspect.getmembers(monster)出来的东西，是形如('__name__', 'monster')
			
			if inspect.isclass(obj):	#把monster中所有类名中的class名提出来
			
				mons.append(name)	#把monster中所有class放入mon列表中
				
		dice = randint(0,len(mons)-1) #dice为骰子
		
		choosen_one = mons[dice]	#随机选择mon中的怪物名（字符串
		
		mon = getattr(monster,choosen_one)

		return mon().attribute()
		
Utility_function().choose_monster_random()