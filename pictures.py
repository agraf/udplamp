#!/usr/bin/env python3

from PIL import Image

star = b'\xff\xff\x00\x10\xff\xff\x00\x40\xff\xff\x00\xa0\xff\xff\x00\x40\xff\xff\x00\x10'

class Pictures:
	def __init__(self):
		self.star = Image.frombytes(mode = "RGBA",
					    size = (5, 1),
					    data = star,
					    decoder_name = "raw")
	
