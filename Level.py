class Level(object):
	""" The Level object, representing
		the state of the game board.
	"""
	def __init__(self, grid):
		super(Level, self).__init__()
		self.contents = grid
