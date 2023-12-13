#!/usr/bin/env python3

from PIL import Image

star_bin = b'\xff\xff\x00\x10\xff\xff\x00\x40\xff\xff\x00\xa0\xff\xff\x00\x40\xff\xff\x00\x10'

class Pictures:
	def __init__(self):
		self.star = Image.frombytes(mode = "RGBA",
					    size = (5, 1),
					    data = star_bin,
					    decoder_name = "raw")
	def hsv_star(self, H = 0, S = 0, V = 0):
		hsv_star = Image.frombytes(mode = "HSV",
					    size = (5, 1),
					    data = bytearray([H % 256, S % 256, V % 256] * 5),
					    decoder_name = "raw")
		star = Image.new(mode = "RGBA",
				  size = (5, 1),
				  color = (0, 0, 0))
		star.paste(hsv_star, (0, 0), self.star)
		return star
		
