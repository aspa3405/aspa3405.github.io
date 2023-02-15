##cowgymnastics

## sample
## 3 4 
## 4 1 2 3
## 4 1 3 2
## 4 2 1 3

import sys

with open("gymnastics.in") as read:
	session_num, cow_num = [int(i)for i in read.readline().split()]
	print(session_num, cow_num)

	sessions = []
	for i in range(session_num):
		sessions.append([int(c) - 1 for c in read.readline().split()])
print(sessions)

#will count the number of consistent pairs.  
counter = 0
# we'll loop through all possible combinations (pairwise) of coes and keep track of considered 
#c1 = first column.  
#c2 = second column.  

for c1 in range(cow_num):
	for c2 in range(cow_num):
		if c1 == c2:
			continue
		print(c1, c2)
        
for s in sessions:
    #print(s.index(c1))
    #print(s.index(c2))
        if s.index(c1) < s.index(c2):
             break
        else:
            counter += 1

print(counter, file = open("gymnastics.out", "w"))