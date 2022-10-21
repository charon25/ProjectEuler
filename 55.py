def iteration(n):
    return n + int(str(n)[::-1])

def is_palindromic(n):
    n_str = str(n)
    return n_str == n_str[::-1]

LIMIT = 10_000

count = 0

for n in range(1, LIMIT):
    for ite in range(50):
        n = iteration(n)
        if is_palindromic(n):
            break
    else:
        count += 1

print(count)
