from math import isqrt

# Solution from https://www.mathblog.dk/project-euler-86-shortest-path-cuboid/

LIMIT = 1_000_000

M = 0
count = 0
while True:
    M += 1
    for wh in range(2, 2 * M + 1):
        sqrt_s = isqrt(M * M + wh * wh)
        if sqrt_s * sqrt_s == M * M + wh * wh:
            count += (wh // 2) if wh <= M else 1 + (M - (wh + 1) // 2)

    if count > LIMIT:
        break

print(M)
