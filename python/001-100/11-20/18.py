import heapq


triangle = []

def neg_int(x):
    return -int(x)

with open('18.txt', 'r') as fi:
    for line in fi:
        triangle.append(list(map(int, line.split(' '))))


WIDTH = max(len(row) for row in triangle)
HEIGHT = len(triangle)

### Method 1 : exhaustive search

PATH_COUNT = 2**(HEIGHT - 1)

biggest_value = 0

for path in range(PATH_COUNT):
    path = bin(path)[2:].zfill(14)
    path_value = triangle[0][0]
    x = 0
    for y in range(HEIGHT - 1):
        if path[y] == '1':
            x += 1
        path_value += triangle[y + 1][x]
    
    if path_value > biggest_value:
        biggest_value = path_value

print(biggest_value)

### Method 2 : dynamic programming

for y in range(1, HEIGHT):
    for x in range(y + 1):
        if x == 0:
            triangle[y][x] = triangle[y][x] + triangle[y - 1][x]
        elif x == y:
            triangle[y][x] = triangle[y][x] + triangle[y - 1][x - 1]
        else:
            triangle[y][x] = triangle[y][x] + max(triangle[y - 1][x - 1], triangle[y - 1][x])

print(max(triangle[HEIGHT - 1]))
