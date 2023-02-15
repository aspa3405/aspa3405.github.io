fileName = open("teleport.in")
dataName = fileName.read().split(" ")
print(dataName)

a = int(dataName[0])
b = int(dataName[1])
x = int(dataName[2])
y = int(dataName[3])

justWalking = abs(b-a)#answer to the problem where the teleporter is not used

teleport = abs(a-x) +abs(b-y)#answer to the problem where the teleporter is used

unnecessary = abs(a-y) +abs(b-x)#answer to the problem where the longest route is taken

Answer = min(justWalking, teleport, unnecessary)#find the minimum output for the equations above

print(Answer, file = open('teleport.out', 'x'))#takes the solution for finding the minimum 
#solution to the problem from each of the equations above, and writes a new file to give 
#the minimum output.  
