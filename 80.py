from decimal import getcontext, Decimal
from math import isqrt

LIMIT = 100

getcontext().prec = 105

total = 0

for n in range(LIMIT):
    if n == isqrt(n) ** 2:
        continue

    sqrt_n = Decimal(n).sqrt()
    sqrt_n = str(sqrt_n).replace('.', '')[:100]
    total += sum(map(int, sqrt_n))

print(total)
