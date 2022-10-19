# Method 1 OEIS

print(145 + 40585)

# Method 2

from math import factorial

factorials = [factorial(k) for k in range(10)]

total = 0

for n in range(10, 100000):
    if n == sum(map(int, [factorials[int(d)] for d in str(n)])):
        total += n

print(total)
