from math import isqrt

# VERY SLOW (30 minutes)

LIMIT = 12_000

# Do not return 1 and n
def get_proper_divisors(n):
    divisors = []
    sqrt_n = isqrt(n)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            divisors.append([i, n // i])
    
    return divisors

DIVISORS = {k: get_proper_divisors(k) for k in range(2, 2 * LIMIT + 1)}

def get_mult_partitioning(n):
    S = [*DIVISORS[n]]

    partitions = set()

    while len(S) > 0:
        part = S.pop()

        partitions.add(tuple(sorted(part)))

        for factor in part:
            divs = DIVISORS[factor]
            if divs:
                new_part = list(part)
                new_part.remove(factor)
                for factor_part in divs:
                    S.append(new_part + factor_part)

    return partitions

PARTITIONS = dict()

for n in range(2, 2 * LIMIT + 1):
    PARTITIONS[n] = get_mult_partitioning(n)

min_prod_sum_nbs = set()

for k in range(2, LIMIT + 1):
    for n in range(k + 1, 2 * k + 1):
        if any(sum(part) + k - len(part) == n for part in PARTITIONS[n]):
            min_prod_sum_nbs.add(n)
            break

print(sum(min_prod_sum_nbs))
