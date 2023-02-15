#Ashley Paulson - Diamond collector Problem
#input code suplied by Anthonyyyyy
#opening input file 
#assign the first line of values to n and m
#then assign the next 6 values to array called diamonds.  
with open('diamond.in') as fin:
	n, k = map(int, fin.readline().split())
	diamonds = [int(fin.readline()) for _ in range(n)]

#this will be final value
value = 0

#for loop to iterate through the values in diamonts do compare them with the inequality stated in the problem.
#value of whihc diamonds can be placed in the case
for i in diamonds:
    showcase = 0
    for j in diamonds:
        if i <= j <= i + k:
            showcase += 1
    value = max(value, showcase)
#value is the max of the two different variables
#outvar should be the final output the problem expects
# (thank you anthony.)  
#open output file with the value 4 printed on it.  
print(value, file = open('diamond.out', 'w'))
