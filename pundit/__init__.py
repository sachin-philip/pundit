import itertools
import json

__version__ = "0.0.6"


'''
PunditBase Parent Class
Arguments : name
'''

class PunditBase():


	def __init__(self):
		self.mine = 'asd'
	

	def input_preprocess(self, id, function):


		def lower(self, id):

			self.processed_input = []
			for x in self.input_set:
				if x['id'] == id:
					self.processed_input.append({'id': x['id'],'value': x['value'].lower(), 'type': x['type']})
				else:
					self.processed_input.append(x)
			return


		def upper(self, id):
			self.processed_input = []
			for x in self.input_set:
				if x['id'] == id:
					self.processed_input.append({{'id': x['id'],'value': x['value'].upper(), 'type': x['type']}})
				else:
					self.processed_input.append(x)
			return

		if function == 'lower':
			lower(self, id)
		elif function == 'upper':
			upper(self, id)
		else:
			pass


	def add_structure(self, arg1, arg2):
		self.structure = []
		self.structure.append({arg1:{}, arg2:{}})


	@property
	def structure(self):
	    return self.structure
	
	

'''
Condition group where conditions are set
'''

class ConditionGroup():

	def __init__(self):
		self.conditions = []


	def add_condition(self, condition, optn, then, else_value):
		input_json = {'condition': condition, 'optn':optn, 'then': then, 'else_value':else_value}
		self.conditions.append(input_json)

	@property
	def conditions(self):
	    return self.conditions
	


'''
Pundit class where structure is defined and 
inherited features of pundit base and condition groups
'''
class Pundit(PunditBase, ConditionGroup):


	def __init__(self, pundit, conditions):
		self.pundit = pundit
		self.conditions = conditions.conditions


	def evaluate(self, input):
		
		#check setup
		type_condition = [x['condition'] for x in self.conditions]

		for x in self.conditions:
			if x['optn'] == 'IN':
				return x['then'] if True in [pd in input for pd in type_condition] else x['else_value']
			else:
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
		
		


