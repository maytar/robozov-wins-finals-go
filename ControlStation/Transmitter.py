import socket
import struct

SERVER_IP = "1.1.1.1"
SERVER_PORT = 4444
PROTO_FAMILY = socket.SOCK_STREAM # SOCK_STREAM or SOCK_DGRAM

pack = lambda x: chr(x)
unpack = lambda x: ord(x)

class Transmitter:
	def __init__(self):
		self.s = socket.socket(socket.AF_INET, PROTO_FAMILY)
		self.s.connect((SERVER_IP, SERVER_PORT))

	def send(self, motors):
		buf = ""
		buf += pack(motors[0])
		buf += pack(motors[1])
		buf += pack(motors[2])

		self.s.send(buf)
