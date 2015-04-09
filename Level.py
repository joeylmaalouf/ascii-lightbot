class Level(object):
	""" The Level object, representing
		the state of the game board.
	"""
	def __init__(self, grid, goal):
		super(Level, self).__init__()
		self.contents = grid
		self.end = goal


if __name__ == "__main__":
	grid = [[0, 0, 1], [-1, 0, 1], [0, 1, 2]]
	lvl1 = new Level(grid, (2, 2))
