largest_palindrome = 1

for a in range(100, 1000):
    for b in range(a, 1000):
        p = a * b
        if p < largest_palindrome:
            continue
        p_str = str(p)
        if p_str == p_str[::-1]:
            largest_palindrome = p

print(largest_palindrome)
