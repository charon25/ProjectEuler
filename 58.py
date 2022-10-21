# The diagonals number can be computed with 4*n^2+(k - 4)+1 where k is 2, 4, 6 or 8 and n = (size - 1) / 2
# When k = 8, the number is a perfect square and therefore does not need to be checked for primality

with open('primes.txt', 'r') as fi:
    primes = set(map(int, fi.read().splitlines()))

from math import isqrt

def is_prime(n):
    for p in range(2, isqrt(n)):
        if n % p == 0:
            return False
    
    return True


size = 1
primes_count = 0
numbers_count = 1
while True:
    size += 2
    n = (size - 1) // 2
    numbers_count += 4
    d1, d2, d3 = [4 * n * n + (k - 4) * n + 1 for k in (2, 4, 6)]
    primes_count += is_prime(d1) + is_prime(d2) + is_prime(d3)

    if 10 * primes_count < numbers_count:
        break

print(size)
