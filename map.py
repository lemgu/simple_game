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
		
			print "-"*50
			utif.Print_attribute(monster).pri()
			utif.Print_attribute(hero).pri()	#输出怪物和英雄的属性
			
			print "-"*50
			
			dict,identifier = utif.Choose_process(hero,monster).specific_choose()	#英雄发起动作,Choose_process(ing,ed）第一个为施加动作的人，第二个为被受到影响的人。这个函数返回的是（属性,返回属性的阵营标识identifier），故根据阵营标识判断返回的属性该赋予给谁
			if identifier == 3:	#identifier的2代表动作施加者，dientifier的3代表动作的承受者
				monster = dict
			elif identifier == 2:
				hero = dict			
				
			print "\n"
			print "-"*50
			print u"结果如下："
			utif.Print_attribute(monster).pri()
			utif.Print_attribute(hero).pri()	#输出怪物和英雄的属性
			print "-"*50
			print "\n"
			
			utif.State_judgement(hero).judge()
			wol = utif.State_judgement(monster).judge()	#wol即"win or lose"
			if wol == "win":
				break	#判断怪物和英雄的状态，若英雄死亡则输出结果，若怪物死亡则退出循环
			
			dict,identifier = utif.Choose_process(monster,hero).random_choose()	#怪物发起随机动作
			
			
			if identifier == 2:
				monster = dict
			elif identifier == 3:
				hero = dict
			
			print "\n"
			print "-"*50
			print u"怪物开始了动作！"
			print u"结果如下："			
			utif.Print_attribute(monster).pri()
			utif.Print_attribute(hero).pri()	#输出怪物和英雄的属性
			print "-"*50
			print "\n"
			
			utif.State_judgement(hero).judge()
			wol = utif.State_judgement(monster).judge()
			if wol == "win":
				break
			
			print u"*****************怪物仍然存活，请继续行动！*******************"
			
		return hero		#返回值为hero的属性值
			
		print u"\n-------------------------------------------------------------------------------------------"	
		print u"\n-------------------------------------------------------------------------------------------"	
		print u"怪物被打败了，你成功通过了这个房间"
		
	def rest_room(self,hero):
	
		room_type = "rest_room"
		
		print u"这是一个休息房"
		print u"你的所有属性增加了当前属性的一半"
		
		hero[u"血量"] = hero[u"血量"] * 1.5
		hero[u"法力值"] = hero[u"法力值"] * 1.5
		hero[u"力量"] = hero[u"力量"] * 1.5
		
		utif.Print_attribute(hero).pri()	#输出怪物和英雄的属性
		
		return hero	#返回值为hero恢复后的的属性值