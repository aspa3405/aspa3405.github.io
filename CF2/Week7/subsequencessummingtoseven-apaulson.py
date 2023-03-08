with open('div7.in') as read:
	cows = [int(read.readline()) for _ in range(int(read.readline()))]

answer = 0

#print(cows)

for i in range(len(cows)):
    cows[i] += cows[i + 1]
print(cows)

# if cows%7 == 0:
#     answer.append()

print(answer)
print(answer, file=open('div7.out', 'w'))
