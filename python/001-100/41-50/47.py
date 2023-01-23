with open('..\\primes.txt', 'r') as fi:
    primes = list(map(int, fi.read().splitlines()))


def get_unique_prime_factors(n):
    factors = dict()
    for prime in primes:
        if n % prime == 0:
            factors[prime] = 0
        while n % prime == 0:
            n //= prime
            factors[prime] += 1
        if n == 1:
            break
    
    return set((prime, factors[prime]) for prime in factors)

COUNT = 4

n = 0
while True:
    n += 1
    if n % 10000 == 0:
        print(n)
    all_factors = [get_unique_prime_factors(n + d) for d in range(COUNT)]
    if all(len(factors) == COUNT for factors in all_factors) and len(all_factors[0].union(*all_factors[1:])) == COUNT * COUNT:
        break

print(n)
