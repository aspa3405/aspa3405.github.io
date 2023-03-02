def psum(a):
    psum = [0]
    for i in a:
        psum.append(psum[-1] + i)
    return psum

#arr = [1, 6, 4, 5, 3]
arr = [1, 10, 100, 1000, 10000] #[4, 11, 20, 35, 55, 78, 108]
print(psum(arr))
psum = psum(arr)
print(psum)

print(psum[3] - psum[2])
print(psum[3] - psum[0])


def reversePsum(p):
    a = [0]
    for i in range(len(p)):
        print(p[i+1]-p[i])
        #a.append()
    return a
p = [0, 4, 11, 20, 35, 55, 78, 108]
reversePsum(p)
