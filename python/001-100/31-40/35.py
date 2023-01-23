with open('..\\primes.txt', 'r') as fi:
    primes = list(map(int, fi.read().splitlines()))

primes_set = set(primes)

def get_cyclic_permutations(string):
    l = len(string)

    for i in range(l):
        yield string[i:] + string[:i]

LIMIT = 1_000_000

count = 4 # 4 primes below 10

for p in primes:
    if p >= LIMIT:
        break

    if p < 10:
        continue

    p = str(p)
    if '0' in p or '2' in p or '4' in 'p' or '5' in p or '6' in p or '8' in p:
        continue

    for perm in get_cyclic_permutations(p):
        perm = int(perm)
        if not perm in primes_set:
            break
    else:
        count += 1

print(count)
