with open('..\\primes.txt', 'r') as fi:
    primes = list(map(int, fi.read().splitlines()))

LIMIT = 50_000_000
LIMIT_PRIME_P2 = int(LIMIT ** 0.5) + 1
LIMIT_PRIME_P3 = int(LIMIT ** (1/3)) + 1
LIMIT_PRIME_P4 = int(LIMIT ** 0.25) + 1

primes_set = set(primes)

numbers = set()

for p4 in primes:
    if p4 > LIMIT_PRIME_P4:
        break
    for p3 in primes:
        if p3 > LIMIT_PRIME_P3:
            break
        for p2 in primes:
            if p2 > LIMIT_PRIME_P2:
                break
            n = p4 ** 4 + p3 * p3 * p3 + p2 * p2
            if n < LIMIT:
                numbers.add(n)

print(len(numbers))
