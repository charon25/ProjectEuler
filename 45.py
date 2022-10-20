from math import sqrt

def is_pentagonal(p):
    n = (1 + sqrt(24 * p + 1)) / 6
    return n % 1 < 1e-09

def is_triangular(t):
    n = (-1 + sqrt(8 * t + 1)) / 2
    return n % 1 < 1e-09

n = 144

while True:
    h = n * (2 * n - 1)
    n += 1

    if is_pentagonal(h) and is_triangular(h):
        break

print(h)
