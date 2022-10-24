from math import gcd

LIMIT = 12000

fractions = set()

for d in range(1, LIMIT + 1):
    for n in range(1, 1 + d // 2):
        g = gcd(n, d)
        a, b = n // g, d // g
        if b < 3 * a and 2 * a < b:
            fractions.add((a, b))

print(len(fractions))
