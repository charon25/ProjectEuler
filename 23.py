from math import isqrt

def divisor_sum(n):
    total = 0
    sqrt_n = isqrt(n)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            total += (i + n // i)
    
    if n == sqrt_n * sqrt_n:
        total -= sqrt_n
    
    return total - n

LIMIT = 20162 # According to OEIS A048242

abudants_number = {n for n in range(1, LIMIT + 1) if n < divisor_sum(n)}

total = 1

for n in range(2, LIMIT):
    found = None

    for a in abudants_number:
        if a >= (n // 2) + 1:
            break
        if n - a in abudants_number:
            found = True
            break

    if not found:
        total += n

print(total)
