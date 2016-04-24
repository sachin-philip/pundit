import itertools
import json

from pundit.base import PunditBase
from pundit.condition import ConditionGroup

__version__ = "0.0.6"


'''
Pundit class where structure is defined and 
inherited features of pundit base and condition groups
'''
class Pundit(PunditBase, ConditionGroup):


	def __init__(self, pundit, conditions):
		self.pundit = pundit
		self.conditions = conditions.conditions


	def evaluate(self, arg1, arg2):

		import ipdb;ipdb.set_trace()
		
		
		if type(input) == str:
			type_condition = [x['condition'] for x in self.conditions]

			for x in self.conditions:
				if x['optn'] == 'IN':
					return x['then'] if True in [pd in input for pd in type_condition] else x['else_value']
				elif x['optn'] == 'NOT_IN':
					return x['then'] if True in [pd in input for pd in type_condition] else x['else_value']
				elif x['optn'] == 'NOT_IS':
					pass
				else:
					return "unsupported operation"
		elif type(input) == int:
			print "integer"
		elif type(input) == list:
			print "list"
		elif type(input) == dict:
			print "dict"
		else:
			print "unsupported format"


		



class MathRuler():
	"""Mathemaical rule operatons"""

	def __init__(self, for_this, then_that):
		self.condition = for_this;
		self.then = then_that


	def math(self, con):
		then_that = self.then
		for_this = self.condition
		exp_converter = then_that.replace(for_this, str(con))
		return eval(exp_converter)	



class ListRuler():
	
	def __init__(self, arg_list):
		self.list = arg_list
		self.reduced = []
		for li in self.list:
			if type(li) == list:
				for cc in list(itertools.chain(li)):
					self.reduced.append(cc)
			else:
				self.reduced.append(li)
		

	def fullfill(self, arg):
		return True if arg in self.reduced else False
		
		


