with open('cowqueue.in') as fin:
  n = fin.readline()
  cows = []
  for line in fin.readlines():
    cows.append(list(map(int, line.split())))
  
print(n)
print(cows)

cur_time = 0



#cur_time should be the final output the problem expects
print(cur_time)
print(cur_time, file=open('cowqueue.out', 'w'))