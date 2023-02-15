#Ashley Paulson Speeding Ticket USACO BRONZE problem Feb 5
# help from Swammer on youtube

#read in files and write the output file
import sys
sys.stdin = open('speeding.in', 'r')

#assign values to n and m
n, m = list(map(int, input().split())) 

#create the values that pertain to the speed limit and create a forloop
speed_lim = [list(map(int,input().split())) for i in range(n)] 

# create the values that pertain to bessues speed
bessies_speed = [list(map(int,input().split())) for i in range(m)]

#set the total to 0
total = 0

#create the lists we can later append
roadspeed = [] 
herspeed = [] 

#set a variable to compare the later calculation to.  
total = 0

#for every value in our above array store the value un roadspeed
for i in speed_lim:
    for j in range(i[0]):
        roadspeed.append(i[1])

#for every value in our above array store the value un herspeed
for i in bessies_speed:
    for j in range(i[0]):
        herspeed.append(i[1])

#for 100 values, compare the values in roadspeed to her speed, 
#take the difference and set it equal to the total if the value is greater.
for i in range(int(100)):
    if roadspeed[i] < herspeed[i] and herspeed[i] - roadspeed[i] > total:
        total = herspeed[i] - roadspeed[i]

print(total, file = open("speeding.out", "w"))
