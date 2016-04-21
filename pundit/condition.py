import itertools
import json

__version__ = "0.0.4"


class PunditBase():
	"""Pundit rule engine to process condisions"""

	def __init__(self, name):
		self.title = name
		self.input_set = []
		self.processed_input = []
		self.condition = []
		


	class Pundit():
		"""Pundit rule engine to process condisions"""

		def __init__(self, name):
			self.title = name
			self.structure = []


		def add_structure(self, arg1, arg2):
			self.structure.append({arg1:{}, arg2:{}})


	class ConditionGroup():
	"""create conditiongroup for pundit object"""

		def __init__(self, name):
			self.name = name
			self.condition = []


		def add_condition(self, condition, optn, then, else_value):
			input_json = {'condition': condition, 'optn':optn, 'then': then, 'else_value':else_value}
			self.condition.append(input_json)
	

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

	
	def evalue():
		pass


	def add_input(self, id, value, type):
		input_json = {'id': id, 'value':value, 'type': type}
		self.input_set.append(input_json) 



	def evaluate(self, type, condition):
		type_condition = [x for x in condition.condition if x['type'] == type]
		process_data = [x['value'] for x in self.processed_input if x['id'] == type]


		for x in type_condition:
			if x['condition'] == 'IN':
				return True if True in [x['value'] in pd for pd in process_data] else False
			else:
				pass




