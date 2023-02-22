#ashley Paulson - Why Did the cow cross the road week 5

#read in input file - thank you Anthony
with open('cowqueue.in') as fin:
  N = fin.readline()
  cows = []
  for line in fin.readlines():
    cows.append(list(map(int, line.split())))
  
#print(N)
#print(cows) These were to check what was being put in each lost from above.

# will come back to this later.  
cur_time = 0 

#using what we learned in class use .sort to get the pairs arranged in array "cows" to ascending order
#and show that it worked ( it does )
cows.sort()
print(cows)

#this loop goes in to the arranged array 'cows' and compares the first value to see if it is greater than 0, 
# then if it is it adds it to our cur_time list which we keep comparing and then we end up with the final value to print later.  
# if it is not then it moves on to the next value. 
for cow in cows:
  if (cur_time > cow[0]):
    cur_time += cow[1]
  else:
    cur_time = cow[0] + cow[1]

#finish and print to a new file called cowqueue.out.  YAY done
print(cur_time)
print(cur_time, file=open('cowqueue.out', 'w'))