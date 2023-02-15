with open('notlast.in') as read:
	raw = {}
	for _ in range(int(read.readline())):
		name, amt = read.readline().split()
		amt = int(amt)
		if name not in raw:
			raw[name] = 0
		raw[name] += amt

cows = [(amt, name) for name, amt in raw.items()]

print(cows)

written = open('notlast.out', 'w')

#find the last arriving cow to find the solution