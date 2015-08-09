class Level(object):
	""" The Level object, representing
		the state of the game board.
	"""
	def __init__(self):
		super(Level, self).__init__()

	def fromfile(self, path = "levels/level01.txt"):
		with open(path, "r") as f:
			s = f.read().replace(" ", "").replace("\t", "")
		grid = [list(row) for row in s.split("\n")]
		self.endpoints = []
		for y, row in enumerate(grid):
			for x, col in enumerate(row):
				if col.isdigit():
					grid[y][x] = int(col) # passable within +-1 height
				elif col == "-":
					grid[y][x] = -1 # impassable
				elif col == "o":
					self.player_start = (y, x, 0)
				elif col == "E":
					self.endpoints.append((y, x))
		self.grid = grid
		return self

	def __str__(self):
		return "\n".join([" ".join(["{0: >2}".format(i) for i in row]) for row in self.grid])


class Player(object):
	""" The Player object, representing the
		state of the human-controlled entity.
	"""
	def __init__(self, pos = (0, 0, 0)):
		super(Player, self).__init__()
		self.pos = pos

	def use_level(self, level):
		self.pos = level.player_start
		self.level = level
		return self

	def move(self, move):
		# pos is row, col, height
		return self


if __name__ == "__main__":
	l4 = Level().fromfile("levels/level04.txt")
	print(l4)
	p = Player().use_level(l4)
	print(p.pos)
