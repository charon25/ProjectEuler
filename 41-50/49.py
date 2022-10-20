with open('..\\primes.txt', 'r') as fi:
    primes = list(map(int, fi.read().splitlines()))

# 4 digits
primes = [prime for prime in primes if 1000 <= prime < 10000]
primes_set = set(primes)

def are_permutations(a, b, c):
    a, b, c = str(a), str(b), str(c)
    return sorted(a) == sorted(b) == sorted(c)

for i, a in enumerate(primes):
    if a == 1487: # We already know it
        continue
    for b in primes[i + 1:]:
        c = 2 * b - a
        if c >= 10000 or not c in primes_set:
            continue
        if are_permutations(a, b, c):
            print(f'{a}{b}{c}')
            exit()
