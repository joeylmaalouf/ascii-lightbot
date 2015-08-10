from copy import deepcopy
from subprocess import call
from sys import argv


class Level(object):
	""" The Level object, representing
		the state of the game board.
	"""
	def __init__(self):
		super(Level, self).__init__()

	def fromfile(self, path = "levels/level00.txt", verbose = False):
		if verbose:
			print("\nLoading level from {0}...".format(path))
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
		if verbose:
			print("Finished loading level.\n")
		return self

	def __str__(self):
		string = "\n".join([" ".join(["{0: >2} ".format(i) for i in row]) for row in self.grid])
		string = string.replace("-1", " -")
		return string

	def __getitem__(self, index):
		if type(index) == type([]):
			return self.grid[index[0]][index[1]] # it's unnecessary to do so, but maybe find a way to extend this for n dimensions?
		else:
			return self.grid[index]

	def __setitem__(self, index, value):
		if type(index) == type([]):
			self.grid[index[0]][index[1]] = value
		else:
			self.grid[index] = value


class Player(object):
	""" The Player object, representing the
		state of the human-controlled entity.
	"""
	def __init__(self, pos = [0, 0]):
		super(Player, self).__init__()
		self.pos = pos
		self.height = 1
		self.orientation = 2 # 0, 1, 2, 3 = N, E, S, W
		self.reached_goal = False

	def move(self, moves, level):
		for move in moves:
			move = move.lower()
			if move == "a": # rotate left
				self.orientation = (self.orientation - 1) % 4
			elif move == "d": # rotate right
				self.orientation = (self.orientation + 1) % 4
			elif move in ["w", "s"]:
				shift = [[-1, 0], [0, 1], [1, 0], [0, -1]][self.orientation]
				forward_space = [self.pos[0] + shift[0], self.pos[1] + shift[1]]
				self.move_to(new_coords = forward_space, jump = move == "s", level = level)
		return self

	def move_to(self, new_coords, jump, level):
		# cannot leave board bounds
		if new_coords[0] < 0 or new_coords[0] > level.rows-1 or new_coords[1] < 0 or new_coords[1] > level.cols-1:
			return self

		value = level[new_coords]
		if value == -1: # can't move here
			pass
		elif value == "S": # starting square has a height of 1
			value = 1 # to allow movement onto it
		elif value == "E": # level won!
			value = [self.height, self.height + 1][jump] # to allow movement onto it
			self.reached_goal = True

		if (not jump) and value == self.height: # move forward
			self.pos = new_coords
		elif jump and value in [self.height + 1, self.height - 1]: # jump forward up or down one level
			self.pos = new_coords
			self.height = value
		return self


class Game(object):
	def __init__(self, player, level):
		super(Game, self).__init__()
		self.player = player
		self.level = level
		self.bounds = ((0, level.rows-1), (0, level.cols-1))
		self.player.pos = list(level.player_start)

	def show_help(self):
		print("Controls:")
		for key, action in zip(["A", "D", "W", "S"], ["Turn left", "Turn right", "move forward", "jump forward up/down"]):
			print("  {0}: {1}".format(key, action))
		print("")
		return self

	def display(self):
		call("clear")
		printable = deepcopy(self.level)
		printable[self.player.pos] = "P"
		print(printable)
		print("Facing: {0}".format(["N", "E", "S", "W"][self.player.orientation]))
		return self

	def run(self):
		self.show_help()
		raw_input("Press enter to start the game.\n")
		while not self.player.reached_goal:
			self.display()
			self.player.move(moves = raw_input("\nMove(s): "), level = self.level)
		self.display()
		print("\nYou win!\n")
		return self


if __name__ == "__main__":
	level = argv[1] if len(argv) > 1 else "0"
	p = Player()
	l0 = Level().fromfile("levels/level{0:0>2}.txt".format(level), verbose = True)
	g = Game(p, l0)
	g.run()
