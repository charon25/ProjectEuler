from itertools import combinations

DIGITS = '0123456789'
SQUARES = [str(n * n).zfill(2) for n in range(1, 10)]

def have_property(d1: tuple[int], d2: tuple[int]):
    for c1, c2 in SQUARES:
        if not (((c1 in d1 or (c1 == '6' and '9' in d1) or (c1 == '9' and '6' in d1)) and (c2 in d2 or (c2 == '6' and '9' in d2) or (c2 == '9' and '6' in d2))) or ((c1 in d2 or (c1 == '6' and '9' in d2) or (c1 == '9' and '6' in d2)) and (c2 in d1 or (c2 == '6' and '9' in d1) or (c2 == '9' and '6' in d1)))):
            return False

    return True

count = 0

for dice1 in combinations(DIGITS, 6):
    for dice2 in combinations(DIGITS, 6):
        if have_property(set(dice1), set(dice2)):
            count += 1

# Everything is counted twice
print(count // 2)
