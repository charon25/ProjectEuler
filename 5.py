BASE_PRIMES = [2, 3, 5, 7]
NON_BASE_PRIMES = [11, 13, 17, 19]

min_count_required = [0 for _ in BASE_PRIMES]

result = 1
for ind, prime in enumerate(BASE_PRIMES):
    for n in range(2, 20 + 1):
        count = 0
        while n % prime == 0:
            n //= prime
            count += 1
        if count > min_count_required[ind]:
            min_count_required[ind] = count

    result *= (prime ** min_count_required[ind])

for prime in NON_BASE_PRIMES:
    result *= prime

print(result)
