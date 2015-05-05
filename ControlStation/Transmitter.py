import socket
import struct

SERVER_IP = "10.2.160.5"
SERVER_PORT = 1234
ADDRESS = (SERVER_IP, SERVER_PORT)
PROTO_FAMILY = socket.SOCK_DGRAM # SOCK_STREAM or SOCK_DGRAM

pack = lambda x: chr(x)
unpack = lambda x: ord(x)

class Transmitter:
	def __init__(self):
		self.s = socket.socket(socket.AF_INET, PROTO_FAMILY)
		# self.s.connect((SERVER_IP, SERVER_PORT))

	def send(self, motors):
		checkNegativity = lambda x: 1 if x > 0 else 0

		buf = ""
		for i in range(3):
			buf += pack(checkNegativity(motors[i]))
			buf += pack(motors[i])

		print buf

		self.s.sendto(buf,ADDRESS)
