from itertools import combinations

with open('primes.txt', 'r') as fi:
    primes = list(map(int, fi.read().splitlines()))

LIMIT = 10**7

PRIME_LIMIT = 10000

primes = [p for p in reversed(primes) if p < PRIME_LIMIT]

correct_n = list()

for p1, p2 in combinations(primes, 2):
    n = p1 * p2
    if n > LIMIT:
        continue
    phi = (p1 - 1) * (p2 - 1)
    if sorted(str(n)) == sorted(str(phi)):
        correct_n.append((n / phi, n))

correct_n.sort()
print(correct_n[0][1])
