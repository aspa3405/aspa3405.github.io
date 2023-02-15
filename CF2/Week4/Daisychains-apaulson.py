#Ashley Paulson Daisy Chains Problem.  

n = int(input())
flowers = list(map(int, input().split()))

# here, you'll do your code to solve the problem.
#this will store the final values 
counter = 0

#probably a poinless array but my code breaks in USACO without it
pairs = []

#nested for loop for every i and j value in pairs array and only print the ones 
#iterates through every i and j value for the inequality given in the problem and then append the probably pointless pairs array
# and then thank you Jack for the help on the average line
#next, iterate x through i "through" j instead of i "to" j.
# break! 
# and it works!! 
for i in range(n):
    for j in range(i,n):
        if(1 <= flowers[i] <= flowers[j] <= n):
            pairs.append([int(flowers[i]), int(flowers[j])])

        average = sum(flowers[i:j + 1]) / (j - i + 1)

        for x in range(i,j + 1):
            if(flowers[x] == average):
                counter += 1
                break
print(counter)



        

#print(counter)
