
#Ashley Paulson - Painting a barn problem - Week 7: 
#Opening code from Anthony:
WIDTH = 1000

barn = [[0 for _ in range(WIDTH + 1)] for _ in range(WIDTH + 1)]
with open('paintbarn.in') as read:
	rect_num, paint_req = [int(i) for i in read.readline().split()]
	for _ in range(rect_num):
		start_x, start_y, end_x, end_y = [int(i) for i in read.readline().split()]
		# Set up the prefix sums array with all the corners of the given rectangle
		barn[start_x][start_y] += 1
		barn[start_x][end_y] -= 1
		barn[end_x][start_y] -= 1
		barn[end_x][end_y] += 1

print(rect_num, paint_req)
#print(barn)
valid_area = 0
#building our prefix sum array
#going through all the x and y values and 
#then in the end we are making sure none of them are larger than 4.  
for x in range(WIDTH + 1):
    for y in range(WIDTH + 1):
        if x > 0:
            barn[x][y] += barn[x-1][y]
        if y > 0:
            barn[x][y] += barn[x][y-1]
        if x > 0 and y > 0:
            barn[x][y] -= barn[x-1][y-1]
        valid_area += barn[x][y] == paint_req

print(barn)
print(valid_area)
print(valid_area, file=open('paintbarn.out', 'w'))