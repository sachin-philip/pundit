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
		self.response = []
		self.set_input = []


	def evaluate(self, arg1, arg2 = None):

		self.set_input.append({self.pundit.arg1: arg1, self.pundit.arg2:arg2})
		
		for yme in self.conditions:

			# type_condition = [x['condition'] for x in self.conditions]
			# for x in self.conditions:
			# import ipdb;ipdb.set_trace()
			if yme['optn'] == 'IN':
				self.response.append(True) if True in [yme['l1'] in  self.set_input[0][yme['arg']]] else self.response.append(False)
			elif yme['optn'] == 'NOT_IN':
				self.response.append(True) if True in [yme['l1'] in  self.set_input[0][yme['arg']]] else self.response.append(False)
			elif yme['optn'] == 'NOT_IS':
				pass
			else:
				return "unsupported operation"
		
		return True if True in self.response else False



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
		
		


