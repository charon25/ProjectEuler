from math import isqrt

def get_proper_divisors(n):
    divisors = [1]
    sqrt_n = isqrt(n)
    for d in range(2, sqrt_n + 1):
        if n % d == 0:
            divisors.append(d)
            divisors.append(n // d)
    
    if n == sqrt_n * sqrt_n:
        divisors.pop()
    
    return divisors

LIMIT = 1_000_000

divisors = {k: get_proper_divisors(k) for k in range(2, LIMIT + 1)}

divisors_sum = dict()
divisors_sum[1] = False
for k in range(2, LIMIT + 1):
    div_sum = sum(divisors[k])
    if div_sum > LIMIT:
        divisors_sum[k] = False
    else:
        divisors_sum[k] = div_sum

chains = []

n = 2
while n <= LIMIT:
    k = n
    chain = list()
    while divisors_sum[k] and not k in chain:
        chain.append(k)
        k = divisors_sum[k]

    if n == k and len(chain) > 1:
        chains.append(chain)

    n += 1

chains.sort(key=lambda chain: (-len(chain), min(chain)))

print(chains[0][0])
