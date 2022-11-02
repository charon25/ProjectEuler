LIMIT = 50

points = set()

for x1 in range(LIMIT + 1):
    for y1 in range(LIMIT + 1):
        if x1 == 0 and y1 == 0:
            continue
        for x2 in range(LIMIT + 1):
            for y2 in range(LIMIT + 1):
                if x2 == 0 and y2 == 0:
                    continue
                if x1 == x2 and y1 == y2:
                    continue

                d1_sq = x1 * x1 + y1 * y1
                d2_sq = x2 * x2 + y2 * y2
                d3_sq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

                d1_sq, d2_sq, d3_sq = sorted((d1_sq, d2_sq, d3_sq))
                if d1_sq + d2_sq == d3_sq:
                    points.add(tuple(sorted(((x1, y1), (x2, y2)))))

print(len(points))
