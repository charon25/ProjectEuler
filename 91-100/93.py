from itertools import permutations, product, combinations

ORDERS = [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 0),
    (2, 0, 0),
    (2, 1, 0)
]

OPERATIONS = list(product((float.__add__, float.__sub__, float.__mul__, float.__truediv__), repeat=3))

def most_consecutives(base_digits):
    base_digits = list(map(float, base_digits))
    results = set()

    for operations in OPERATIONS:
        for order in ORDERS:
            for digits in permutations(base_digits):
                dig = list(digits)
                ops = list(operations)
                for ind in order:
                    try:
                        res = ops[ind](dig[ind], dig.pop(ind + 1))
                    except ZeroDivisionError:
                        dig = None
                        break
                    dig[ind] = res
                    ops.pop(ind)

                if dig and dig[0] % 1 == 0 and dig[0] > 0:
                    results.add(int(dig[0]))

    results = sorted(results)
    for a, b in zip(results, results[1:]):
        if b - a > 1:
            return a

best_consec = 0
best_digits = None

for base_digits in combinations(list(range(1, 10)), 4):
    most_consec = most_consecutives(base_digits)
    if most_consec > best_consec:
        best_consec = most_consec
        best_digits = base_digits

print(''.join(map(str, best_digits)))
