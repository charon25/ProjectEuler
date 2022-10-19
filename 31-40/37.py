# Method 1 : OEIS A020994

l = [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]

print(sum(l))

# Method 2

with open('..\\primes.txt', 'r') as fi:
    primes = list(map(int, fi.read().splitlines()))

primes_set = set(primes)

def is_right_truncatable_prime(p):
    p = str(p)
    while p:
        if not int(p) in primes_set:
            return False
        p = p[:-1]
    
    return True

def is_left_truncatable_prime(p):
    p = str(p)
    while p:
        if not int(p) in primes_set:
            return False
        p = p[1:]
    
    return True

LIMIT = 1_000_000

total = 0

for p in primes:
    if p < 10:
        continue
    if p >= LIMIT:
        break

    if is_left_truncatable_prime(p) and is_right_truncatable_prime(p):
        total += p

print(total)
