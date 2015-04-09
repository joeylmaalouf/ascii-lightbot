class LightBot(object):
	""" The LightBot object, representing
		the player-directed character.
	"""
	def __init__(self, directions):
		super(LightBot, self).__init__()
		self.moves = list(directions)
		self.position = (0, 0)
		self.bearing = 'N'
		self.height = 0

	def travel():
		for direction in self.directions:
			self.handleDirection(direction)

	def handleDirection(direction):
		if direction == 'w':
			self.moveForward()
		elif direction == 's':
			self.moveBackward()
		elif direction == 'a':
			self.turnLeft()
		elif direction == 'd':
			self.turnRight()
		elif direction == 'u':
			self.jumpUp()
			self.moveForward()
		elif direction == 'j':
			self.jumpDown()
			self.moveForward()
		else:
			print "Unknown direction: ", direction

	def moveForward():
		r, c = self.position
		if self.bearing == "N":
			r = r - 1
		elif self.bearing == "E":
			c = c + 1
		elif self.bearing == "S":
			r = r + 1
		elif self.bearing == "W":
			c = c - 1
		else:
			print "Unknown bearing: ", self.bearing

		self.position = (r, c)

	def moveBackward():
		r, c = self.position
		if self.bearing == "N":
			r = r + 1
		elif self.bearing == "E":
			c = c - 1
		elif self.bearing == "S":
			r = r - 1
		elif self.bearing == "W":
			c = c + 1
		else:
			print "Unknown bearing: ", self.bearing

		self.position = (r, c)

	def turnLeft():
		if self.bearing == "N":
			self.bearing = "W"
		elif self.bearing == "W":
			self.bearing = "S"
		elif self.bearing == "S":
			self.bearing = "E"
		elif self.bearing == "E":
			self.bearing = "N"
		else:
			print "Unknown bearing: ", self.bearing

	def turnRight():
		if self.bearing == "N":
			self.bearing = "E"
		elif self.bearing == "E":
			self.bearing = "S"
		elif self.bearing == "S":
			self.bearing = "W"
		elif self.bearing == "W":
			self.bearing = "N"
		else:
			print "Unknown bearing: ", self.bearing

	def jumpUp():
		self.height = self.height + 1

	def jumpDown():
		self.height = self.height - 1

