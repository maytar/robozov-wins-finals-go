from Transmitter import Transmitter

class InputMethod:
	def __init__(self):
		self.motor_speeds = [0, 0, 0]
		# Init transmitter
		self.t = Transmitter()

	def doListenLoop(self):
		while True:
			self.getInput()
			self.t.send(self.motor_speeds)

	def getInput(self):
		pass