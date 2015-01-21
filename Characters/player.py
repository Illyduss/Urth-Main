
from .character import *
from Items.container import *

class Player(Character):
	def __init__(self, name, hp, str, int, loc):
		Character.__init__(self, name, hp, str)
		self.str = str
		self.int = int
		self.loc = loc
		self.name = name

		self.inventory = set()

	def die(self, message="Game Over!"):
		print(message)
		self.hp = 0
		self.dead = True
		input()	
