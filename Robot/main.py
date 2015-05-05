from socket import *
from BrickPi import *
import struct

SERVER_PORT = 1234
MAX_SPEED = 255
SPEED_FOR_PERCENT = 255/100.0

MESSAGE_SIZE = 6

LEFT_WHEEL = PORT_A # Left wheel motor
RIGHT_WHEEL = PORT_B # Right wheel motor
NET_MOTOR = PORT_C # The motor to leap the net
motors = [LEFT_WHEEL, RIGHT_WHEEL, NET_MOTOR]

s = socket(AF_INET, SOCK_DGRAM)
s.bind(("", SERVER_PORT))

BrickPiSetup()
for i in motors:
	BrickPi.MotorEnable[i] = 1

while True:
	(data,addr) = s.recvfrom(MESSAGE_SIZE)
	if len(data) != MESSAGE_SIZE:
		continue

	for i in xrange(0, MESSAGE_SIZE, 2):
		sign = ord(data[i])
		sign = -1 if sign == 1 else 1
		val = ord(data[i+1])
		val = int(val*sign*SPEED_FOR_PERCENT)

		BrickPi.MotorSpeed[i/2] = val

	BrickPiUpdateValues()


