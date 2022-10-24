with open('primes.txt', 'r') as fi:
    primes = list(map(int, fi.read().splitlines()))

primes_set = set(primes)
PRIMES_COUNT = len(primes)

LIMIT = 1_000_000


# Method 1

def phi(n):
    if n in primes_set:
        return n - 1
    
    factors = prime_factors(n)
    product = 1
    for p in factors:
        product *= (p - 1) * (p**(factors[p] - 1))

    return product


def prime_factors(n):
    factors = dict()

    ind = 0
    p = primes[ind]
    while n > 1 and ind < PRIMES_COUNT:
        if n % p == 0:
            factors[p] = 0
            while n % p == 0:
                factors[p] += 1
                n //= p
        ind += 1
        p = primes[ind]
    
    if n == 1:
        return factors
    
    p += 1
    while n > 1:
        if n % p == 0:
            factors[p] = 0
            while n % p == 0:
                factors[p] += 1
                n //= p
        p += 1
    
    return factors

ratio_max = 0
n_max = 0

for n in range(2, LIMIT + 1):
    ratio = n / phi(n)
    if ratio > ratio_max:
        ratio_max = ratio
        n_max = n

print(n_max)

# Method 2

def n_over_phi(n):
    if n in primes_set:
        return n - 1
    
    factors = unique_prime_factors(n)
    product = 1
    for p in factors:
        product *= 1 / (1 - 1 / p)

    return product


def unique_prime_factors(n):
    factors = list()

    ind = 0
    p = primes[ind]
    while n > 1 and ind < PRIMES_COUNT:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        ind += 1
        p = primes[ind]
    
    if n == 1:
        return factors
    
    p += 1
    while n > 1:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    
    return factors


ratio_max = 0
n_max = 0
from tqdm import tqdm
for n in tqdm(range(2, LIMIT + 1)):
    ratio = n_over_phi(n)
    if ratio > ratio_max:
        ratio_max = ratio
        n_max = n

print(n_max)
