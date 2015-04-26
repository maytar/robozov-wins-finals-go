from InputMethod import InputMethod

class KeyboardInputMethod(InputMethod):
	def __init__(self):
		InputMethod.__init__(self)

	def getInput(self):
		inp = (raw_input(">>") + 'aaa')[:3]
		self.motor_speeds = [(lambda c: (0 if c=='a' else 100))(c) for c in inp]
