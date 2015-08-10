class Level(object):
	""" The Level object, representing
		the state of the game board.
	"""
	def __init__(self):
		super(Level, self).__init__()

	def fromfile(self, path = "levels/level00.txt"):
		with open(path, "r") as f:
			s = f.read().replace(" ", "").replace("\t", "")
		grid = [list(row) for row in s.split("\n")]
		self.rows, self.cols = len(grid), len(grid[0])
		for y, row in enumerate(grid):
			for x, col in enumerate(row):
				if col.isdigit(): # passable within +-1 height
					grid[y][x] = int(col)
				elif col == "-": # impassable
					grid[y][x] = -1
				elif col == "S": # player start
					self.player_start = (y, x)
				elif col == "E": # goal
					self.goal = (y, x)
		self.grid = grid
		return self

	def __str__(self):
		return "\n".join([" ".join(["{0: >2}".format(i) for i in row]) for row in self.grid])

	def __getitem__(self, index):
		if type(index) == type([]):
			return self.grid[index[0]][index[1]]
		# for convenience
		return self.grid[index]


class Player(object):
	""" The Player object, representing the
		state of the human-controlled entity.
	"""
	def __init__(self, pos = [0, 0]):
		super(Player, self).__init__()
		self.pos = pos
		self.height = 1
		self.orientation = 2 # 0, 1, 2, 3 = N, E, S, W
		self.won = False

	def use_level(self, level):
		# if level is a string, generate the level object ourselves from that path
		if type(level) == type(""):
			level = Level().fromfile(level)
		# otherwise, assume it's a pre-created level object
		self.pos = list(level.player_start)
		self.level = level
		return self

	def show_on_level(self):
		tmp = self.level[self.pos[0]][self.pos[1]]
		self.level[self.pos[0]][self.pos[1]] = "P"
		print(self.level)
		self.level[self.pos[0]][self.pos[1]] = tmp
		return self

	def move(self, moves):
		for move in moves:
			move = move.lower()
			if move == "a": # rotate left
				self.orientation = (self.orientation - 1) % 4
			elif move == "d": # rotate right
				self.orientation = (self.orientation + 1) % 4
			elif move in ["w", "s"]:
				shift = [[-1, 0], [0, 1], [1, 0], [0, -1]][self.orientation]
				forward_space = [self.pos[0] + shift[0], self.pos[1] + shift[1]]
				self.move_to(new_coords = forward_space, jump = move == "s")
		return self

	def move_to(self, new_coords, jump = False):
		# cannot leave board bounds
		if new_coords[0] < 0 or new_coords[0] > self.level.rows-1 or new_coords[1] < 0 or new_coords[1] > self.level.cols-1:
			return self

		value = self.level[new_coords]
		if value == -1: # can't move here
			pass
		elif value == "S": # starting square has a height of 1
			value = 1 # to allow movement onto it
		elif value == "E": # level won!
			value = [self.height, self.height + 1][jump] # to allow movement onto it
			self.won = True # do stuff with this flag later, make some sort of game input loop that gets broken out of?

		if (not jump) and value == self.height: # move forward
			self.pos = new_coords
		elif jump and value in [self.height + 1, self.height - 1]: # jump forward up or down one level
			self.pos = new_coords
			self.height = value
		return self


if __name__ == "__main__":
	p = Player().use_level("levels/level00.txt")
	p.show_on_level()
	p.move("ww")
	print("")
	p.show_on_level()
