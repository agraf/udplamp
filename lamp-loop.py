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

# Wir wollen einen Stern auf das Bild packen. Der Ort vom Stern ist
# allerdings flexibel. In dieser Variable merken wir uns, wo der Stern
# gerade ist.
x = 0

while True:
	# "image" wird unser Bild für diesen Durchlauf. Wir fangen an mit
	# einem Bild das 250 Pixel breit und 1 Pixel hoch ist. Es beginnt
	# mit jedem Pixel als als Rot=0, Grün=0, Blau=0, also schwarz.
	image = Image.new(mode = "RGB",
			  size = (250, 1),
			  color = (0, 0 ,0))

	# Wir fügen einen Stern an Pixel x hinzu.
	image.paste(pics.star, (x, 0), pics.star)

	# Jede Runde geht der Stern um einen Pixel weiter
	x = x + 1
	if x > 250:
		x = 0

	# Jetzt schicken wir das neue Bild an den LED-Streifen
	lamp.set(image)

	# und warten eine zehntel Sekunde bis zum nächsten Bild.
	time.sleep(0.1)
