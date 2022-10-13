# Method 1
S = 0
a, b = 1, 1
while b < 4000000:
    a, b = b, a + b
    if b % 2 == 0:
        S += b

print(S)

# Method 2

from math import sqrt

s5 = sqrt(5)
phi = (s5 + 1) / 2

print(f'{(5 - s5) / 20 * (phi ** 36 - 1) - (5 + s5)/20:.0f}')
