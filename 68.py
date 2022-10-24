# Shape
# 0    1
#   2
# 3   4
#5
#  6 7   8
#   9
# Diagonals : 0-2-4, 1-4-7, 8-7-6, 9-6-3, 5-3-2

from itertools import permutations

L = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

ORDERINGS = {
    0: (0, 2, 4, 1, 4, 7, 8, 7, 6, 9, 6, 3, 5, 3, 2),
    1: (1, 4, 7, 8, 7, 6, 9, 6, 3, 5, 3, 2, 0, 2, 4),
    8: (8, 7, 6, 9, 6, 3, 5, 3, 2, 0, 2, 4, 1, 4, 7),
    9: (9, 6, 3, 5, 3, 2, 0, 2, 4, 1, 4, 7, 8, 7, 6),
    5: (5, 3, 2, 0, 2, 4, 1, 4, 7, 8, 7, 6, 9, 6, 3)
}

def is_magic(l):
    s = l[0] + l[2] + l[4]

    if l[1] + l[4] + l[7] != s:
        return False

    if l[8] + l[7] + l[6] != s:
        return False

    if l[9] + l[6] + l[3] != s:
        return False

    if l[5] + l[3] + l[2] != s:
        return False

    return True

def get_str(l):
    min_leaf = min((i for i in (0, 1, 8, 9, 5)), key=lambda i:l[i])
    ordering = ORDERINGS[min_leaf]
    return ''.join(map(str, (l[ind] for ind in ordering)))

strings = []

for perm in permutations(L):
    if is_magic(perm):
        string = get_str(perm)
        if len(string) == 16:
            strings.append(int(get_str(perm)))

print(max(strings))
