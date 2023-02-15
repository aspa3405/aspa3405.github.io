with open('cowqueue.in') as fin:
  N = fin.readline()
  cows = []
  for line in fin.readlines():
    cows.append(list(map(int, line.split())))
  
#print(N)
#print(cows)

cur_time = 0

cows.sort()
#print(cows)

for i in range(len(cows)):
  #print(cows[i][start])
  #print(cows[i][duration])
  sequence = []  
  if (cows[0][0] + cows[0][1]) < cows[1][0]:
    #print(cows[1][0])
    sequence.append(cows[1][0]+cows[1][1])
    #print(sequence)
    if(str(sequence))>(str(cows[2][0]+cows[2][1])):
      sequence.append(str(cows[2][1]))
      #print(sequence)
  cur_time = int(sequence[0]) + int(sequence[1])
#cur_time should be the final output the problem expects
print(cur_time)
print(cur_time, file=open('cowqueue.out', 'w'))