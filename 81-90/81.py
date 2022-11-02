matrix = []

with open('81.txt', 'r') as fi:
    for line in fi:
        matrix.append(list(map(int, line.split(','))))

HEIGHT = len(matrix)
WIDTH = len(matrix[0])

graph = dict()
weights = dict()
for y in range(HEIGHT):
    for x in range(WIDTH):
        weights[(x, y)] = matrix[y][x]
        neighbors = []
        if y < HEIGHT - 1:
            neighbors.append((x, y + 1))
        if x < WIDTH - 1:
            neighbors.append((x + 1, y))
        graph[(x, y)] = neighbors

SOURCE = (0, 0)
TARGET = (WIDTH - 1, HEIGHT - 1)

dist = dict()
prev = dict()
Q = list()
for v in graph:
    dist[v] = 100000000 * WIDTH * HEIGHT
    prev[v] = None
    Q.append(v)

dist[(0, 0)] = 0

while len(Q) > 0:
    u = min(Q, key=lambda v:dist[v])
    Q.remove(u)

    for v in graph[u]:
        alt = dist[u] + weights[v]
        if alt < dist[v]:
            dist[v] = alt
            prev[v] = u

total_cost = 0

u = TARGET
while u is not None:
    total_cost += weights[u]
    u = prev[u]

print(total_cost)
