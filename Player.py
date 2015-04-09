class LightBot(object):
	""" The LightBot object, representing
		the player-directed character.
	"""
	def __init__(self, directions):
		super(LightBot, self).__init__()
		self.moves = list(directions)
		self.location = (0, 0)
		self.direction = 'N'
		self.height = 0

	def travel():
		for direction in directions:
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
		elif direction == 'j':
			self.jumpDown()
		else:
			print "Unknown direction: ", direction

	def moveForward():
		r, c = self.position
		if self.direction == "N":
			r = r - 1
		elif self.direction == "E":
			c = c + 1
		elif self.direction == "S":
			r = r + 1
		elif self.direction == "W":
			c = c - 1
		else:
			print "Unknown direction: ", self.direction

		self.position = (r, c)

	def moveBackward():
		r, c = self.position
		if self.direction == "N":
			r = r + 1
		elif self.direction == "E":
			c = c - 1
		elif self.direction == "S":
			r = r - 1
		elif self.direction == "W":
			c = c + 1
		else:
			print "Unknown direction: ", self.direction

		self.position = (r, c)

	def turnLeft():
		if self.direction == "N":
			self.direction = "W"
		elif self.direction == "W":
			self.direction = "S"
		elif self.direction == "S":
			self.direction = "E"
		elif self.direction == "E":
			self.direction = "N"
		else:
			print "Unknown direction: ", self.direction

	def turnRight():
		if self.direction == "N":
			self.direction = "E"
		elif self.direction == "E":
			self.direction = "S"
		elif self.direction == "S":
			self.direction = "W"
		elif self.direction == "W":
			self.direction = "N"
		else:
			print "Unknown direction: ", self.direction

	def jumpUp():
		self.height = self.height + 1

	def jumpDown():
		self.height = self.height - 1


