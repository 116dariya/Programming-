from PIL import Image, ImageDraw
im = Image.open("01.jpg")
rgb_im = im.convert("RGB")
size = rgb_im.size
a, f = size
pix = rgb_im.load()
depth = int(input('depth:'))
for y in range(0, size[1]):
	for x in range(0, size[0]):
		r, g, b = pix[x, y]
		s = (r + g + b) // 3
		r = s + k * 2
		g = s + k
		b = s
		pix[x, y] = (r, g, b)

rgb_im.save("11.jpg")