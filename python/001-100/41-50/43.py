from itertools import permutations

PRIMES = (2, 3, 5, 7, 11, 13, 17)

def has_property(string):
    for i, p in enumerate(PRIMES, start=1):
        if int(string[i:i+3]) % p != 0:
            return False

    return True

total = 0

for perm in permutations('0123456789'):
    if perm[0] == '0':
        continue

    n_str = ''.join(perm)
    if has_property(n_str):
        total += int(n_str)

print(total)

