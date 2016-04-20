import itertools
import json

__version__ = "0.0.3"


class Pundit():
	"""Pundit rule engine to process condisions"""

	def __init__(self, name):
		self.title = name
		self.input_set = []
		
	def add_input(self, id, value, type):
		input_json = {'id': id, 'value':value, 'type': type}
		self.input_set.append(input_json) 

	def add_condition(self):
		pass

	@property
	def input_preprocess(self, id, func):
		input_dict = json.loads(self.input_set)

		def lower():
			pass

	def evaluate(self):
		pass


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
		
		


