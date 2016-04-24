import json


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
		self.arg1 = arg1
		self.arg2 = arg2
		self.structure.append({arg1:{}, arg2:{}})


	@property
	def structure(self):
	    return self.structure
	
	
