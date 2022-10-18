from itertools import permutations

l = list(range(10))
perm = permutations(l)

n = 0
while n < 1000000:
    n += 1
    permutation = next(perm)

print(''.join(map(str, permutation)))
