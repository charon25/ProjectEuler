with open('primes.txt', 'r') as fi:
    primes = list(map(int, fi.read().splitlines()))

LIMIT = 1_000_000

primes = [prime for prime in primes if prime < LIMIT]
primes_set = set(primes)

# Compute length of longest sequence possible

total = 0
n = 0
while total < LIMIT:
    total += primes[n]
    n += 1

LONGEST_SEQUENCE = n

# Solve exercice

for length in range(LONGEST_SEQUENCE, 0, -1):
    start = 0
    seq_sum = sum(primes[:length])
    while seq_sum < LIMIT:
        if seq_sum in primes:
            print(seq_sum)
            exit()
        seq_sum = seq_sum - primes[start] + primes[start + length]
        start += 1
