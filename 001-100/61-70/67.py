import heapq


triangle = []

def neg_int(x):
    return -int(x)

with open('67.txt', 'r') as fi:
    for line in fi:
        triangle.append(list(map(int, line.split(' '))))


WIDTH = max(len(row) for row in triangle)
HEIGHT = len(triangle)

for y in range(1, HEIGHT):
    for x in range(y + 1):
        if x == 0:
            triangle[y][x] = triangle[y][x] + triangle[y - 1][x]
        elif x == y:
            triangle[y][x] = triangle[y][x] + triangle[y - 1][x - 1]
        else:
            triangle[y][x] = triangle[y][x] + max(triangle[y - 1][x - 1], triangle[y - 1][x])

print(max(triangle[HEIGHT - 1]))
