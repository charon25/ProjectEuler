TARGET = 2_000_000
LIMIT = 2000 + 1 # Should be enough to find the answer as rect_count(2000, 1) > TARGET

# Method 1

def rect_count(n, m):
    return (n * (n + 1) * m * (m + 1)) // 4


best_diff = TARGET
best_nm = None

for n in range(1, LIMIT):
    for m in range(1, n + 1):
        count = rect_count(n, m)
        diff = abs(count - TARGET)
        if diff < best_diff:
            best_diff = diff
            best_nm = (n, m)

print(best_nm[0] * best_nm[1])

# Method 2

from math import sqrt

best_decimal_part = 1
best_nm = None

for n in range(1, LIMIT):
    dn = (n * (n + 1))
    m = (sqrt((16 * (TARGET) + dn) / dn) - 1) / 2
    decimal_part = m % 1
    if decimal_part < best_decimal_part:
        best_decimal_part = decimal_part
        best_integer = (n, int(round(m, 0)))

print(best_integer[0] * best_integer[1])
