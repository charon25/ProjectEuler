with open('primes.txt', 'r') as fi:
    primes = list(map(int, fi.read().splitlines()))

from math import isqrt

primes_set = set(primes)

n = 1

while True:
    n += 2

    if n in primes_set:
        continue

    has_property = False
    for p in primes:
        if p > n - 2:
            break
        sq = (n - p) // 2
        sqrt = isqrt(sq)
        if sqrt * sqrt == sq:
            has_property = True
    
    if not has_property:
        break

print(n)
