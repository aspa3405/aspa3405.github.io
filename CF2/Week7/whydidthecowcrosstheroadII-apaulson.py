#Ashley Paulson - Why did the cow cross the road II - Week 7
#Opening code from Anthony Pinter

#read in the file MaxCross.in and split each balue and append 
with open('maxcross.in') as read:
	n, k, b = map(int, read.readline().split())
	seen = [0] * (n + 1)
	left, right = 1, k
	value = 0
	
	for _ in range(b):
		seen[int(read.readline())] = 1

#print(n, k, b)
#print(seen)

#set up value to append later with the minimum value!
answer = 0
#make sure that K is always larger
#hold the length of k
for i in range(left, right + 1):
	value += seen[i]
#set up the prefix sum to append each value as the for loop below increases each value and subtracts it. 
#set up value to append later with the minimum value! 
psum = [value]
#check to see how many values equalling 1 there are in the arrangement.  
while n > right:  
	#the sum of the current + previous
	value += seen[right + 1] - seen[left]
	#keep moving along the array
	left, right = left + 1, right + 1
	#calculate and add the amount of 1's in the array 
	psum.append(value)
#from the array in the forloop, find the smallest one. That is your answer.  
answer = min(psum)

print(answer, file=open('maxcross.out', 'w'))
