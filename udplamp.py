#!/usr/bin/env python3

import socket

class UdpLamp:
	def __init__(self, ip):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.ip = ip

	def set(self, img):
		b = img.tobytes()
		print(b)
		self.sock.sendto(b, (self.ip, 1235))
