TEN_DIGITS = 10**10

# Method 1

print(sum(k**k for k in range(1, 1000 + 1)) % TEN_DIGITS)

# Method 2

print(sum((k**k) % TEN_DIGITS for k in range(1, 1000 + 1)) % TEN_DIGITS)

# Method 3

total = 0

for k in range(1, 1000 + 1):
    sub_total = 1
    for i in range(k):
        sub_total = (sub_total * k) % TEN_DIGITS
    
    total += sub_total

print(total % TEN_DIGITS)
