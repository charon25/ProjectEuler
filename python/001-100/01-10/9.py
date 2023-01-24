# Method 1

from math import isqrt

for a in range(1, 1000 + 1):
    for b in range(a, 1000 + 1):
        c2 = a * a + b * b
        c = isqrt(c2)
        if a + b + c == 1000 and c ** 2 == c2:
            print(a, b, c)
            print(a * b * c)

# Method 2

from math import sqrt

# Useless to check before 415 as the square root is complex
for c in range(415, 1000 + 1):
    a = 0.5 * sqrt(c * c + 2000 * c - 1_000_000) - c / 2 + 500
    if a % 1 == 0:
        a = int(a)
        b = 1000 - c - a
        if b > 0:
            print(a * b * c)
