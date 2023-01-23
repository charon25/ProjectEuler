from collections import deque
from itertools import product

FUNCTIONS = {
    3: lambda n: (n * (n + 1)) // 2,
    4: lambda n: n * n,
    5: lambda n: (n * (3 * n - 1)) // 2,
    6: lambda n: (n * (2 * n - 1)),
    7: lambda n: (n * (5 * n - 3)) // 2,
    8: lambda n: (n * (3 * n - 2))
}

polygons_str = {k: [] for k in FUNCTIONS}

n = 1
too_big = [False for _ in polygons_str]
while not all(too_big):
    for k in polygons_str:
        value = FUNCTIONS[k](n)
        if value >= 10000:
            too_big[k - 3] = True
            continue
        if value >= 1000:
            polygons_str[k].append(str(value))

    n += 1

polygon_by_number_str: dict[str, list[int]] = {str(n): [] for n in range(1000, 10000)}
for k in polygons_str:
    for number_str in polygons_str[k]:
        polygon_by_number_str[number_str].append(k)


COUNT = 6
TARGET = [k + 3 for k in range(COUNT)]

def has_property(l: list[str]):
    length = len(l)
    for a, b in zip(l, l[1:]):
        if a[2:] != b[:2]:
            return False

    if length == COUNT and l[-1][2:] != l[0][:2]: # Compare the last and the first only if we have a complete sequence
        return False

    polygons_prod = product(*[polygon_by_number_str[a] for a in l])
    return any(len(set(polygon)) == length for polygon in polygons_prod)


all_polygons_str = []
for k in polygons_str:
    all_polygons_str.extend(polygons_str[k])

all_polygons_str = sorted(set(all_polygons_str))
all_polygons_str_set = set(all_polygons_str)

polygons_count = len(all_polygons_str)

stack = deque((polygon,) for polygon in all_polygons_str)

while len(stack) > 0:
    seq = stack.popleft()

    if len(seq) == COUNT - 1:
        last = seq[-1][2:] + seq[0][:2]
        if last in all_polygons_str_set:
            new_seq = seq + (last,)
            if has_property(new_seq):
                print(sum(map(int, new_seq)))
                break
    
    for new_polygon in all_polygons_str:
        if new_polygon in seq:
            continue
        new_seq = seq + (new_polygon,)
        if has_property(new_seq):
            stack.appendleft(seq + (new_polygon,))
