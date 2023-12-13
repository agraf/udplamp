#!/usr/bin/env python3

from PIL import Image
from udplamp import UdpLamp

lamp = UdpLamp('192.168.107.10')

image = Image.new(mode = "RGB",
		  size = (250, 1),
		  color = (0, 0 ,0))

lamp.set(image)
