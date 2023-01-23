from math import isqrt

LIMIT = 2_000_000
MAX_CHECK = isqrt(LIMIT) + 1

sieve = [False for _ in range(LIMIT)]
sieve[0] = True
sieve[1] = True

for n in range(2, MAX_CHECK):
    if sieve[n]:
        continue

    for d in range(2 * n, LIMIT, n):
        sieve[d] = True

print(sum(n for n, is_composite in enumerate(sieve) if not is_composite))
