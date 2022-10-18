def S(size):
    n = (size - 1) // 2
    return (2 * (n + 1) * (8 * n * n + 7 * n + 6)) // 3 - 3

print(S(1001))
