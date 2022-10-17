N0 = N = 600851475143

p = 2
largest_factor = p
while p * p < N0:
    if N % p == 0:
        N //= p
        largest_factor = p
    else:
        p += 1

print(largest_factor)
