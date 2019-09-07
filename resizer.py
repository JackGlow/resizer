import os, sys
import time
from PIL import Image

print("Resizer starts his job...")
size = 256,256 # ENTER NEEDED SIZE WIDTH/HEIGHT
path = "\\" # ENTER YOUR PATH TO FOLDER WITH IMAGES HERE
totalpngs = 0
pathlist = os.listdir(path)
for f in pathlist:
		if(f.endswith(".png")):
			totalpngs += 1
			try:
				im = Image.open(path + "\\" + f)
				ima = im.resize(size, Image.NEAREST)
				ima.save(path + "\\" + f, "PNG")
			except IOError:
				print("fukkk")

print("Total PNGs: " + str(totalpngs) + "/" + str(len(pathlist)))
