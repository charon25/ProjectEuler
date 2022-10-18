# Method 1 : OEIS A063990

l = [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]

print(sum(l))

# Method 2

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

sums = {0: 0}
amicable = []

for n in range(1, 10000 + 1):
    div_sum = divisor_sum(n)
    sums[n] = div_sum
    if div_sum < n and sums[div_sum] == n:
        amicable.append(n)
        amicable.append(div_sum)

print(sum(amicable))
