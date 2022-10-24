with open('primes.txt', 'r') as fi:
    primes = list(map(int, fi.read().splitlines()))

LIMIT = 1_000_000

sieve = [1 for _ in range(LIMIT + 1)]
sieve[0] = 0

for p in primes:
    if p > LIMIT + 1:
        break
    sieve[p] = p - 1

    for d0 in range(2 * p, LIMIT + 1, p):
        k = 0

        d = d0
        while d % p == 0:
            k += 1
            d //= p

        sieve[d0] *= (p - 1) * (p ** (k-1))


print(sum(sieve) - 1) # OEIS A015614
