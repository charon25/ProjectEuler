from itertools import permutations
from math import isqrt

def is_prime(n):
    if n in (2, 3, 5, 7):
        return True

    if n == 1 or n % 10 in (0, 2, 4, 5, 6, 8):
        return False

    sqrt_n = isqrt(n)

    for k in range(3, sqrt_n + 1):
        if n % k == 0:
            return False

    return True

biggest_pandigital_prime = 0

for n in range(1, 10):
    digits = ''.join(str(k) for k in range(1, n + 1))
    for perm in permutations(digits):
        perm = int(''.join(perm))
        if perm <= biggest_pandigital_prime:
            continue
        if is_prime(perm):
            biggest_pandigital_prime = perm

print(biggest_pandigital_prime)
