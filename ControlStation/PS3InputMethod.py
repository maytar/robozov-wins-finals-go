import sixaxis
from InputMethod import InputMethod
from time import sleep
	

class PS3InputMethod(InputMethod):
	
	def __init__(self, path):
		sixaxis.init(path)
		InputMethod.__init__(self)

	def getInput(self):
		state = sixaxis.get_state()
		self.motor_speeds[0] = int(state['lefty'] )
		self.motor_speeds[1] = int(state['righty'] )
		self.motor_speeds[2] = int(state['trig2'] )
		print self.motor_speeds
		sleep(0.1)
		

	
