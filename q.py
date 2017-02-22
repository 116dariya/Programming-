s = input()
l = []
for c in s:
	if c == '(' or c == '{' or c == '[':
		l.append(c)
	else:
		if len(l) > 0:
			k = l.pop()
			if k == '[' and c == ']':
				l.pop()
			if k == '{' and c == '}':
				l.pop()
			if k == '(' and c == ')':
				l.pop()
print(len(l))
print(l)


