# -*- coding: utf-8 -*-

import map
import utif
import process
import attribute
import json #为了等会打印中文字典的时候应用其dumps模块，不出现乱码


the_count = [1]

class Engine(object):
	
	# def __init__(self):
	
	def game_run(self):
		
		hero1 = attribute.Attribute().attri()	#创建人物
		
		print u"你的人物初始属性是："
		# print json.dumps(hero1,encoding = 'utf-8',ensure_ascii = False) #josn.dumps（）将字典dicts转化为字符串string，于是可以顺利输出。但是这种方法不够好（字典无序，故输出无序，所以我采用下面的方法）
		
		utif.utility_function().print_attri(hero1)	#输出人物的属性
		
		next = map.Map().monster_room()
		

		
		for num in the_count:
			
			print "-"*50
			
			monster1 = Utility_function().judge_room(next)		#判断房间类型
			
			print u"你打算做什么?\n 1:[物理攻击] 2:[法术攻击] 3:[金币贿赂]"
			
			doing = int(raw_input(">"))
			

			
			utif.Utility_function().judge_move(hero1,monster1,doing)
			
			print u"你的属性："
			utif.Utility_function().print_attri(hero1)
			print u"怪物的属性："
			utif.Utility_function().print_attri(monster1)
			
			utif.Utility_function().judge_attri(hero1,u"英雄")
			utif.Utility_function().judge_attri(monster1,u"怪物")
			
			
			
			
			
			
		
game_start = Engine().game_run()