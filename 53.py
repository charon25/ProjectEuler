from math import comb

LIMIT = 1_000_000

count = 0

for n in range(1, 100 + 1):
    for r in range(n + 1):
        if comb(n, r) > LIMIT:
            count += 1

print(count)
