with open('primes.txt', 'r') as fi:
    primes = list(map(int, fi.read().splitlines()))

primes_set = set(primes)

def get_length_consecutive(a, b):
    n = 0
    while True:
        p = n * (n + a) + b
        if not p in primes_set:
            return n
        n += 1

longest_ab = None
longest = 0

# b only in primes because of n = 0
for b in primes:
    if b >= 1000:
        break

    for a in range(-999, 1000):
        # Case for n = 1
        if not (a + b + 1) in primes_set:
            continue

        length = get_length_consecutive(a, b)
        if length > longest:
            longest = length
            longest_ab = (a, b)

print(longest_ab[0] * longest_ab[1])
