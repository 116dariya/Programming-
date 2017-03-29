from PIL import Image, ImageDraw
im = Image.open("01.jpg")
rgb_im = im.convert("RGB")
size = rgb_im.size
a, f = size
pix = rgb_im.load()
max_color = 0, 0, 0
max_value = 0
colors = {}
for y in range(0, size[1]):
	for x in range(0, size[0]):
		r, g, b = pix[x, y]
		r = r // 5
		g = g // 5
		b = b // 5
		if r + g + b < 50:
			continue 
		if (r, g, b) in colors:
			colors[r, g, b] += 1
		else:
			colors[r, g, b] = 1
for k in colors:
	r, g, b = k
	value = colors[r, g, b]
	if value > max_value:
		max_color = (r, g, b)
		max_value = value

print(max_color)
for y in range(0, size[1]):
	for x in range(0, size[0]):
		r, g, b = pix[x, y]
		s = (r + g + b) // 3
		r = min(s + max_color[0]*1 + 40, 128)
		g = min(s + max_color[1]*1 + 20, 128) 
		b = min(s + max_color[2]*1, 128)
		pix[x, y] = (r, g, b)

rgb_im.save("11.jpg")