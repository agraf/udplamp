#!/usr/bin/env python3

from PIL import Image
from udplamp import UdpLamp
from pictures import Pictures
import time

# "lamp" ist das Objekt um die Lampe anzusteuern
lamp = UdpLamp('192.168.107.10')

# In "pics" sind vorgebaute Bilder, die man auf das Bild kopieren kann.
# Aktuell gibt es nur pics.star als Stern.
pics = Pictures()

# Wir wollen einen Stern mit sich ändernder Farbe auf das Bild packen.
# Dafür bestimmen wir farben im "HSV" Farbraum. Wir beginnen mit 0/0/0.
h = 0
s = 0
v = 0

while True:
	# "image" wird unser Bild für diesen Durchlauf. Wir fangen an mit
	# einem Bild das 250 Pixel breit und 1 Pixel hoch ist. Es beginnt
	# mit jedem Pixel als als Rot=0, Grün=0, Blau=0, also schwarz.
	image = Image.new(mode = "RGB",
			  size = (250, 1),
			  color = (0, 0, 0))

	# Wir generieren uns einen andersfarbigen Stern
	hsv_star = pics.hsv_star(h, s, v)

	# Wir fügen diesen Stern an Pixel 5 hinzu.
	image.paste(hsv_star, (5, 0), hsv_star)

	# Jede Runde Ändern wir h, s und v.
	h = h + 3
	s = s + 2
	v = v + 1

	# Jetzt schicken wir das neue Bild an den LED-Streifen
	lamp.set(image)

	# und warten eine hundertstel Sekunde bis zum nächsten Bild.
	time.sleep(0.01)
