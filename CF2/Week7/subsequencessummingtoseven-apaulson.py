# with open('div7.in') as read:
# 	cows = [int(read.readline()) for _ in range(int(read.readline()))]

# answer = 0

# #print(cows)

# for i in range(len(cows)):
#     cows[i] += cows[i + 1]
# print(cows)

# # if cows%7 == 0:
# #     answer.append()

# print(answer)
# print(answer, file=open('div7.out', 'w'))
MOD = 7

with open('div7.in') as read:
	cows = [int(read.readline()) for _ in range(int(read.readline()))]

best_photo = 0
# first_occ[i] stores the index of the first time a prefix sum % 7 == i
first_occ = [-1 for _ in range(MOD)]
first_occ[0] = 0

running_mod = 0
for v, c in enumerate(cows):
	running_mod = (running_mod + c) % MOD

	if first_occ[running_mod] == -1:
		first_occ[running_mod] = v
	else:
		best_photo = max(best_photo, v - first_occ[running_mod])

print(best_photo)
print(best_photo, file=open('div7.out', 'w'))