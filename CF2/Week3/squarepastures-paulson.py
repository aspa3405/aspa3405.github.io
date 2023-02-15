import sys # lets us open specific functions and parameters.  
sys.stdin = open("square.in", "r") #open the square.in file and READ IT
sys.stdout = open("square.out", "w") #makes an output file and WRITES IT 

x1, y1, x2, y2 = map(int, input().split()) #create integers from the values in each line of square.in using mapping
#transforming each value into an integer.  
x3, y3, x4, y4 = map(int, input().split()) #create more integers from the values

# 
left = min(x1, x3) #length 1 * width 3
right = max(x2, x4) #length 2 * width 4
bottom = min(y1, y3)#length 1 * width 3
top = max(y2, y4)#length 2 * width 4

# equation that shows which side length is smallest
side = max(right - left, top - bottom) # find largest side and 
print(side * side) # multiply the side lengths to get a big enough field 
#PRINT it on output file - square.out woooohoooo