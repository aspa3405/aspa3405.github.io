
#Ashley Paulson Milk Pails 
#input and output code provided by Anthony

with open('pails.in') as fin:
	buck1, buck2, order = map(int, fin.readline().split())
 
#print(buck1, buck2, order)

outvar = 0

#(checks all numbers from 0 - 77)
for first in range(order + 1):
    x = buck1 * first
    if x > order:
        break
    
    for second in range(order + 1):
        current = (buck1 * first) + (buck2 * second)
        if current > order:
            break
        outvar = max(outvar, current)#outvar should be the final value output

print(outvar, file = open('pails.out', 'w'))
