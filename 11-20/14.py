memory = {}

longest_chain = 1
longest_n0 = None

LIMIT = 1_000_000

n0 = 1
for n0 in range(1, LIMIT + 1):
    length = 0
    n = n0
    while n > 1:
        if n in memory:
            length += memory[n] - 1
            break
        if n % 2 == 0:
            n //= 2
            length += 1
        else:
            n = (3 * n + 1) // 2
            length += 2

    memory[n0] = length + 1

    if length + 1 > longest_chain:
        longest_chain = length + 1
        longest_n0 = n0

    n0 += 1

print(longest_n0)
