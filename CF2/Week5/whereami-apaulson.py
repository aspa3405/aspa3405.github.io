#Ashley Paulson - week 5 problem "Where am I?"
# go through to check all the different k positions

#assign n and mailboxes
#make line 1 an integer, n: the number of mailboxes, and make line 2 a string, ABCDABC: the string of mailboxes. 

file_in = open('whereami.in')
data = file_in.read().strip().split('\n')
n = int(data[0])
mailboxes = data[1]

print(n)
print(mailboxes)

ans = 1

for k in range(1, n+1):
    print("K is: " + str(k))

    sequence = set()
    #print(sequence)

    for i in range(n - k + 1):
        # check from 0 -> n - k + 1
        # k - 3 -> check 0,1,2,3,4
        #print(i)
        sequence.add(mailboxes[i : i + k])
        #print(sequence)
        #print(len(sequence))
        #print(n-k+1)

    if len(sequence) == (n - k + 1):
        #print(len(sequence))
        #print(n - k + 1)
        #n is always 7
        #k = 3 -> 7 - 3 + 1 = 5
        ans = k
        # we can exit the loop as this will be the smallest working length
        break
    
print(ans, file = open('whereami.out', 'w'))