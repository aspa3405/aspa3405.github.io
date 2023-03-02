#Ashley Paulson Subsequencessummingtosevens (Canvas problem 1)
#Intro Code from Anthony Pinter.

with open('div7.in') as read:
	cows = [int(read.readline()) for _ in range(int(read.readline()))]

answer = 0

#print(cows)

# Implement a prefix sum to fo through and figure out if each combo is perfectly divisible by seven using MOD %
psum = [-1 for _ in range(7)]
psum[0] = 0

# enumerate - adds a counter to the iteration and then is used for a loop woohooo
# loop through each value in the prefix sum above and mod 7

arr = 0
for i, j in enumerate(cows): 
	arr = (arr + j) % 7
# if it is negative, move on from that value
# i becmes the values that are divisible by 7 and then subtract all of the one that are not! 
	if psum[arr] == -1:
		psum[arr] = i
	else:
		answer = max(answer, i - psum[arr])
#print the answer in a file alled div7.out
print(answer)
print(answer, file=open('div7.out', 'w'))