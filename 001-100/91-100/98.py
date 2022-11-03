from itertools import combinations, permutations
from math import isqrt

with open('98.txt', 'r') as fi:
    words = fi.read().replace('"', '').split(',')

letters = {}

for word in words:
    key = tuple(sorted(word))
    letters[key] = letters.get(key, []) + [word]

pairs: list[tuple[str, str]] = []

for anagrams in letters.values():
    if len(anagrams) <= 1:
        continue

    pairs.extend(combinations(anagrams, r=2))

squares = []
from tqdm import tqdm
for w1, w2 in tqdm(pairs):
    unique = sorted(set(w1))
    first_letters = set((w1[0], w2[0]))
    for digits in permutations('0123456789', r=len(unique)):
        new_w1 = w1
        new_w2 = w2
        for i, digit in enumerate(digits):
            # No leading zero
            if unique[i] in first_letters and digit == '0':
                break

            new_w1 = new_w1.replace(unique[i], digit)
            new_w2 = new_w2.replace(unique[i], digit)
        else:
            n1 = int(new_w1);sqrt_n1 = isqrt(n1)
            n2 = int(new_w2);sqrt_n2 = isqrt(n2)
            if n1 == sqrt_n1 * sqrt_n1 and n2 == sqrt_n2 * sqrt_n2:
                squares.extend((n1, n2))

print(max(squares))
