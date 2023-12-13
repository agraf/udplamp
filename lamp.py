#!/usr/bin/env python3

from PIL import Image
from udplamp import UdpLamp
from pictures import Pictures

# "lamp" ist das Objekt um die Lampe anzusteuern
lamp = UdpLamp('192.168.107.10')

# In "pics" sind vorgebaute Bilder, die man auf das Bild kopieren kann.
# Aktuell gibt es nur pics.star als Stern.
pics = Pictures()

# "image" wird unser Bild für diesen Durchlauf. Wir fangen an mit
# einem Bild das 250 Pixel breit und 1 Pixel hoch ist. Es beginnt
# mit jedem Pixel als als Rot=0, Grün=0, Blau=0, also schwarz.
image = Image.new(mode = "RGB",
		  size = (250, 1),
		  color = (0, 0 ,0))

# Wir fügen einen Stern an Pixel 5 hinzu.
image.paste(pics.star, (5, 0), pics.star)

# Jetzt schicken wir das neue Bild an den LED-Streifen
image.show()
#lamp.set(image)
