import sys


class Level(object):
	""" The Level object, representing
		the state of the game board.
	"""
	def __init__(self, grid, goal):
		super(Level, self).__init__()
		if len(grid) < 1:
			print("Error: Cannot create a level of grid size 0.")
			sys.exit()
		for row in grid:
			for val in row:
				if not -1 <= val <= 9:
					print("Error: Block heights must all be between -1 and 9 (inclusive).")
					sys.exit()
		self.grid = grid
		self.goal = goal

	def __str__(self):
		string = ""
		rows = len(self.grid)
		cols = len(self.grid[0])

		hbar = "+---"*cols+"+\n"
		vbars = "|   "*cols+"|\n"
		lvlbars = []
		for i in range(rows):
			s = ""
			for j in range(cols):
				s += "|{0:2d} ".format(self.grid[i][j])
			s += "|\n"
			lvlbars.append(s)

		for i in range(rows):
			string += hbar
			string += vbars
			string += lvlbars[i]
			string += vbars
		string += hbar

		return string


if __name__ == "__main__":
	grid = [[0, 0, 1], [-1, 0, 1], [0, 1, 2], [1, 2, 2]]
	lvl1 = Level(grid, (2, 2))
	print(lvl1)
