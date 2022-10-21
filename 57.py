# Continued fraction of sqrt(2) is of the recurring form : 
# u(n+1) = 1 + 1 / (1 + u(n)) where u(0) = 1
# If we express u(n) = a(n) / b(n), we can show that u(n+1) = (2b(n) + a(n)) / (b(n) + a(n))
# which means a(n+1) = 2b(n) + a(n) and b(n+1)=a(n) + b(n) with a(0) = b(0) = 1
# We just have to compute these and check when a(n) has more digits than b(n)

from math import log10

LIMIT = 1000

count = 0

a, b = 1, 1
for _ in range(LIMIT):
    a, b = 2 * b + a, b + a
    if int(log10(a)) + 1 > int(log10(b)) + 1:
        count += 1

print(count)
