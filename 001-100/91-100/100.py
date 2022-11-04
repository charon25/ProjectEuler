from functools import lru_cache
from math import sqrt

# OEIS A046090
# Gives every integer N such that N² + (N - 1)² is a perfect square
# it can be proven that this is enough to have ((b / N) * (b - 1) / (N - 1)) = 1/2
@lru_cache
def a(n):
    if n == 0:
        return 1
    if n == 1:
        return 4
    
    return 6 * a(n - 1) - a(n - 2) - 2

LIMIT = 10**12

n = 1
while a(n) < LIMIT:
    n += 1

N = a(n)
b = int((1 + sqrt(N * N + (N + 1) * (N + 1))) // 2)

print(b)
