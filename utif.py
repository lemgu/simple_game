# -*- coding: utf-8 -*-

#工具函数

from random import randint
import process
import monster
import inspect	#inspect 模块用于等会用于查找文件中的类
from sys import exit


class Choose_monster(object):
	
	def choose_monster_random(self):	
	
		"""随机选取怪物房的怪物"""
		
		mons = []
		
		all = inspect.getmembers(monster)	#查找monster中的所有模块名
		
		for name,obj in all:	#inspect.getmembers(monster)出来的东西，是形如('__name__', 'monster')
			
			if inspect.isclass(obj):	#把monster中所有类名中的class名提出来
			
				mons.append(name)	#把monster中所有class放入mon列表中
				
		dice = randint(0,len(mons)-1) #dice为骰子
		
		choosen_one = mons[dice]	#随机选择mon中的怪物名（字符串
		
		mon = getattr(monster,choosen_one)

		return mon().attribute()
		
		
class Print_attribute(object):

	"""按顺序打印生物属性"""

	def __init__(self,attri):
	
		self.blood = attri[u"血量"]
		self.mana = attri[u"法力值"]
		self.strength = attri[u"力量"]
		self.money = attri[u"金币"]
		self.camp = attri[u"阵营"]
		
	def pri(self):
		
		if self.camp == 0:
			
			print u"本方的属性值为：{| 血量:%d | 法力值:%d | 力量:%d | 金币:%d |}" %(self.blood,self.mana,self.strength,self.money)
			
		elif self.camp == 1:
		
			print u"对方的属性值为：{| 血量:%d | 法力值:%d | 力量:%d | 金币:%d |}" %(self.blood,self.mana,self.strength,self.money)
			
			
class Choose_process(object):
	
	"""生物选择其行动，并输出被影响者的作用后属性"""
	
	def __init__(self,ing,ed):	#ing表示选择动作的生物，ed表示被动作作用的生物，此处的ing与ed均为字典（生物属性）
	
		self.ing = ing
		self.ed = ed
		
	def print_choice(self):
		
		print u"请问你要做什么？"
		
		print u"|| 1:物理攻击 || 2:法术攻击 || 3:龟缩防御 || 4:贿赂逃跑 ||"
		
	def move(self,option):	
	
		if option == 1:
					
			kill = process.Process(self.ing).attack()
			self.ed[u"血量"] = self.ed[u"血量"] + kill
			
			return self.ed,3	#前面的为返回了被作用者的属性，后面的为返回属性值的归属标识（3为承受者，2为施加者）
			
			
		elif option == 2:
				
			destory = process.Process(self.ing).manadestory()
			self.ed[u"血量"] = self.ed[u"血量"] + destory
			
			return self.ed,3	
		
		elif option == 3:
					
			armor = process.Process(self.ing).define()
			self.ing[u"血量"] = self.ing[u"血量"] + armor
			
			return self.ing,2
		
		elif option == 4:
		
			final = process.Process(self.ing).run()
			
			if final == "success":
			
				self.ed[u"血量"] = 0
				
				print "\n"
				print u"**************************************"
				print u"*************逃跑成功*****************"
				print u"**************************************"
				
				
			elif final == "fail":
				
				print "\n"
				print u"**************************************"
				print u"*************逃跑失败*****************"
				print u"**************************************"
				
			return self.ed,3
			
			
	#---------------------------------两种选择行为的方式----------------------------------------------------------------
		
	def random_choose(self):
	
		dice = randint(1,3)		
		return self.move(dice)	#直接把被作用者被作用后的属性值传递出去，此处在引用该函数时，应当赋值给被作用者（全局变量）		
	
	def specific_choose(self):
	
		self.print_choice()
		print "\n"
		choose = int(raw_input(">你的选择是？（输入对应数字）：".decode('utf-8').encode('gbk')))
		
		return self.move(choose)	#直接把被作用者被作用后的属性值传递出去，此处在引用该函数时，应当赋值给被作用者（全局变量）	
		
class dead(object):

	"""根据对应阵营，输出死亡结果"""

	def __init__(self):
	
		pass
		
	def death(self,camp):
	
		if	camp == 0:
	
			print u"【你死了】" 
			
			exit(0)
			
		elif camp == 1:
		
			print u"))))))))))))))))))))))【对方死了】((((((((((((((((((((((((((((((("
			
			return "win"

class State_judgement(object):

	"""判断生物状态属性（暂为只判断是否死亡）,并作出应有回应"""
	
	def __init__(self,attri):	#dict为生物的属性
		
		self.blood = attri[u"血量"]
		self.mana = attri[u"法力值"]
		self.strength = attri[u"力量"]
		self.money = attri[u"金币"]
		self.camp = attri[u"阵营"]
		
	def judge(self):
	
		if self.blood <= 0:
		
			return dead().death(self.camp)
			
			
			
			
			
			
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		