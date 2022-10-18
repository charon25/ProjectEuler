# Method 1

a, b = 1, 1
n = 2
while b < 10**999:
    a, b = b, a + b
    n += 1

print(n)

# Method 2

from math import sqrt, log, ceil

phi = (1 + sqrt(5)) / 2
n = (0.5 * log(5) + 999 * log(10)) / log(phi)

print(ceil(n))
