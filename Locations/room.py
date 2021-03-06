
import json
import os
from test import *

def getRoom(id):
	base_dir = os.path.dirname(__file__)
	filename = str(id)+".json"
	abs_file = os.path.join(base_dir, filename)
	ret = None
	with open(abs_file, "r") as f:
		jsontext = f.read()
		d = json.loads(jsontext)
		d['id'] = id
		ret = Room(**d)
	return ret

class Room():
	def __init__(self, id=0, name="A Room", description="An empty room.", description2="A dark and empty room.", neighbors={}):
		self.id = id
		self.name = name
		self.neighbors = neighbors
		if counter == 1:   
        		self.description = description
    		elif counter == 2:
        		self.description = description2
		else:
			self.description = "Sorry, counter not at 1 or 2!"

	def _neighbor(self, direction):
		if direction in self.neighbors:
			return self.neighbors[direction]
		else:
			return None

	def north(self):
		return self._neighbor('n')

	def northeast(self):
		return self._neighbor('ne')

	def east(self):
		return self._neighbor('e')

	def southeast(self):
		return self._neighbor('se')

	def south(self):
		return self._neighbor('s')

	def southwest(self):
		return self._neighbor('sw')

	def west(self):
		return self._neighbor('w')

	def northwest(self):
		return self._neighbor('nw')

	def up(self):
		return self._neighbor('u')

	def down(self):
		return self._neighbor('d')
