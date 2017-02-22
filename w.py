s = input()
l = s.split( )
m = []
for c in l:
	if c not in ['+' , '-' , '*']:
		m.append(c)
	if c in ['+' , '-' , '*']:
		if len(m) >= 2:
			a = int(m.pop())
			b = int(m.pop())
			if c == '+':
				k = a + b
			if c == '-':
				k = b - a
			if c == '*':
				k = a * b
			m.append(k)

print(m[0])
  

x = True
y = False
z = False

if x or y and z:
print("yes")
else:
print("no")