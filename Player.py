class LightBot(object):
	""" The LightBot object, representing
		the player-directed character.
	"""
	def __init__(self, directions):
		super(LightBot, self).__init__()
		self.moves = list(directions)
