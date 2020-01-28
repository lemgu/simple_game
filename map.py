# -*- coding: utf-8 -*-

import monster
import process
import utif

class Map(object):
	
	def monster_room(self,hero):	#这个hero指的是hero的属性（即一个字典）
	
		room_type = "monster_room"
		
		print u"你将面临一个怪物" 
		print u"尝试去击败他"
		
		monster = utif.Choose_monster().choose_monster_random()	#生成随机的怪物monster，此处的monster为一个字典
		
		while True:
			
			utif.Print_attribute(monster).pri()
			print "-"*50
			utif.Print_attribute(hero).pri()	#输出怪物和英雄的属性
			
			monster = utif.Choose_process(hero,monster).specific_choose()	#Choose_process(ing,ed）第一个为施加动作的人，第二个为被受到影响的人。这个函数返回的是被影响的人的属性，故赋值给monster
		
		
		