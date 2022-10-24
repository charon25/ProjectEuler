LIMIT = 1_000_000

min_diff = 1
num_min = None

for d in range(1, LIMIT + 1):
    n = (3 * d - 1) // 7
    if 0 <= 3/7 - n/d < min_diff:
        min_diff = 3/7 - n/d
        num_min = n

print(num_min)
