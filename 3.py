from PIL import Image, ImageDraw
im = Image.open("i.jpg")
rgb_im = im.convert("RGB")
size = im.size
new_im = im.resize((50, 50))
new_im.save("pasportnew.jpg")
size = new_im.size
pix = new_im.load()
r1 = 212
g1 = 169
b1 = 135
counter = 0
for y in range(0, size[1]):
	for x in range(0, size[0]):
		r, g, b = pix[x, y]
		if (abs(r - r1) + abs(g - g1) + abs(b - b1)) < 20:
			counter = counter + 1

			

print(counter)