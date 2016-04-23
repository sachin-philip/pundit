import json


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