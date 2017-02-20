s = input()
s = s.split(" ")
n = []
o = []
for c in s:

	if c.isnumeric():
		n.append(c)
	elif c is "+" or "-":
		if "*" in o or "/" in o:
			a = o.pop()
			n.append(a)
			o.append(c)
		elif "+" in o or "-" in o:
			a = o.pop()
			n.append(a)
			o.append(c)
		else:
			o.append(c)
	elif c is "*" or "/":
		if "*" in o or "/" in o:
			a = o.pop()
			n.append(a)
			o.append(c)
			
		else:
			o.append(c)
	elif c is "(":
		o.append(c)
	elif c is ")":
		o.append(c)
		while a != "(":
			a = o.pop()
			n.append(a)
			o.append(c)
			
while len(o) != 0:
	a = o.pop()
	n.append(a)

print(n)