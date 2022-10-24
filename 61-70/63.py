from math import log10

count = 0

# This is the condition necessary to have a n-digit integer which is a n-th power
# As 10^n always has n+1>n digits, the base must be <= 9, so we only need to check when 9^n has n digits or more
n = 1
while int(n * log10(9)) + 1 >= n:
    for b in range(1, 10):
        if int(n * log10(b)) + 1 == n:
            count += 1
    n += 1

print(count)
