#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP

def send(msg):
	sock.sendto(msg, ('192.168.107.10', 1235))

msg = bytearray()
for i in range(250):
  if i > 80 and i < 90:
    msg.append(0)
    msg.append(0)
    msg.append(0)
  elif i > 140 and i < 200:
    msg.append(0)
    msg.append(0)
    msg.append(0)
  else:
    msg.append(i)
    msg.append(100)
    msg.append(0)

send(bytes(msg))
