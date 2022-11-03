from math import sqrt

def is_pentagonal(p):
    n = (1 + sqrt(24 * p + 1)) / 6
    return n % 1 < 1e-09

i = 1
while True:
    pi = (i * (3 * i - 1)) // 2
    i += 1

    for j in range(i-1, 0, -1):
        pj = (j * (3 * j - 1)) // 2
        if (is_pentagonal(pi - pj) and is_pentagonal(pi + pj)):
            print(pi - pj)
            exit()
