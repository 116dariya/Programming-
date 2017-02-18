s = input()
s = s.split(" ")
n = []
o = []
for c in s:
	if c.isnumeric():
		n.append(int(c))
	if c is "+" or "-":
		if "*" in o or "/" in o:
			a = o.pop()
			n.append(a)
		elif "+" in o or "-" in o:
			a = o.pop()
			n.append(a)
		else:
			o.append(c)
	if c is "*" or "/":
		if "*" in o or "/" in o:
			a = o.pop()
			n.append(a)
		else:
			o.append(c)
	if c is "(":
		o.append(c)
	if c is ")":
		while a != "(":

			a = o.pop()
			n.append(a)


print(n)