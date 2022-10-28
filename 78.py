TARGET = 1_000_000

# Method 1 (https://www.mathblog.dk/project-euler-78-coin-piles/)

n = 0
WAYS = [1]
while True:
    n += 1
    i = 0
    pentagonal = 1
    ways = 0

    while pentagonal <= n:
        sign = -1 if i % 4 > 1 else 1
        ways += sign * WAYS[n - pentagonal]
        i += 1

        j = -(i // 2 + 1) if i % 2 else i // 2 + 1
        pentagonal = (j * (3 * j - 1)) // 2
    
    WAYS.append(ways)

    if ways % TARGET == 0:
        break

print(n)

# Method 2 : too slow

from math import isqrt

SIGMA = {}
WAYS = {}

def sigma(n):
    if n in SIGMA:
        return SIGMA[n]

    sqrt_n = isqrt(n)
    s = 1 + n
    for d in range(2, sqrt_n + 1):
        if n % d == 0:
            s += (d + (n // d))
    
    if n == sqrt_n * sqrt_n:
        s -= sqrt_n
    
    SIGMA[n] = s
    return s

def count_ways(n):
    if n in WAYS:
        return WAYS[n]
    if n == 0:
        return 1

    ways = sum(sigma(n - k) * count_ways(k) for k in range(n)) // n

    WAYS[n] = ways

    return ways

n = 1
while True:
    n += 1
    ways = count_ways(n)
    if n % 1000 == 0:
        print(n)
    if ways % TARGET == 0:
        break

print(ways)
