from math import ceil, log

N = 10001

LIMIT = ceil(N * (log(N) + log(log(N))))

sieve = [False for _ in range(LIMIT)]

prime_found = 0

for n in range(2, LIMIT):
    if sieve[n]:
        continue

    prime_found += 1
    if (prime_found == N):
        print(n)
        break

    for d in range(2 * n, LIMIT, n):
        sieve[d] = True

