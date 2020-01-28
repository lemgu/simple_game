# -*- coding: utf-8 -*-

from random import randint
import map
import hero
import utif
import process
import attribute
import json #为了等会打印中文字典的时候应用其dumps模块，不出现乱码




class Engine(object):
	
	def __init__(self,the_count,room):
	
		self.the_count = the_count
		self.room = room
	
	def game_run(self):
		
		heros = hero.Hero_random().attribute()	#创建人物
		print "\n"
		print u"你的人物初始属性是："
		# print json.dumps(hero1,encoding = 'utf-8',ensure_ascii = False) #josn.dumps（）将字典dicts转化为字符串string，于是可以顺利输出。但是这种方法不够好（字典无序，故输出无序，所以我采用下面的方法）
		
		utif.Print_attribute(heros).pri()	#输出人物的属性
		
		for num in self.the_count:
		
			print "\n"
			print "-"*50
			print u"**************进入房间*****************"
			
			room_dice = randint(0,len(self.room)-1)
			
			room_type = self.room[room_dice]	#随机房间
			
			room = getattr(map.Map(),room_type)
			
			heros = room(heros)	#room()的返回值为英雄的属性值（详见map中，房间的返回值）
			
		print "\n"
		print "-"*50
		print u"**************游戏结束，你成功赢得了胜利！*****************" 
			
the_count = [1,2,3,4,5,6,7,8,9,10]
room = ["monster_room","rest_room"]		

game_start = Engine(the_count,room).game_run()