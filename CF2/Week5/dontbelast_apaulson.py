#ashley Paulson - Dont Be Last week 5
#this is the opening code from Anthony, reading in the values from the input function notlast.in 
#arranging them into arrays. "raw" and "cows"

with open('notlast.in') as read:
	raw = {}
	for _ in range(int(read.readline())):
		name, amt = read.readline().split()
		amt = int(amt)
		if name not in raw:
			raw[name] = 0
		raw[name] += amt

cows = [(amt, name) for name, amt in raw.items()]
#sort the array
cows.sort()

#print(cows)
#set this variable up to be appended in the for loop
i = 0
#this if statement measures the length of the array and if the length is 7, then 
#finding the cow that prints the second to least amount of milk or print "tie"    
if len(cows) == 7:
	while(i < len(cows) and cows[i][0] == cows[0][0]):
		i += 1
if (i < len(cows) and (i + 1 == len(cows) or cows[i][0] != cows[i+1][0])):
	smaller = cows[i][1]
else: 
	smaller = "tie"

#finish up and print out the new file "notlast.out"
print(smaller, file = open("notlast.out", "w"))