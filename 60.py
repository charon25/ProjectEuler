from collections import deque
from math import isqrt

with open('primes.txt', 'r') as fi:
    primes_str = fi.read().splitlines()

primes_str.pop(2) # 5
primes_str.pop(0) # 2

primes_str_set = set(primes_str)

def is_prime(n_str):
    if n_str in primes_str_set:
        return True
    
    n = int(n_str)

    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    
    for p in range(11, isqrt(n)):
        if n % p == 0:
            return False
    
    return True

def has_property(l):
    for i, p1 in enumerate(l):
        for j, p2 in enumerate(l):
            if i != j:
                if not is_prime(p1 + p2) or not is_prime(p2 + p1):
                    return False
    
    return True

lengths = {p_str: len(p_str) for p_str in primes_str}

LIMIT = 10_000 # Enough
COUNT = 5

primes_str = [prime for prime in primes_str if int(prime) < LIMIT]
primes_count = len(primes_str)

stack = deque((k, (prime,)) for k, prime in enumerate(primes_str))

while len(stack) > 0:
    index, seq = stack.popleft()

    if len(seq) == COUNT:
        print(sum(map(int, seq)))
        break
    
    for new_index in range(primes_count - 1, index, -1):
        new_prime = primes_str[new_index]
        new_seq = seq + (new_prime,)
        if has_property(new_seq):
            stack.appendleft((new_index, seq + (new_prime,)))

