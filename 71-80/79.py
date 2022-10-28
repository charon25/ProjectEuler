with open('79.txt', 'r') as fi:
    codes = fi.read().splitlines()

pairs = set()
digits = set()

for code in codes:
    digits.update(code)
    pairs.add(code[:2])
    pairs.add(code[1:])
    pairs.add(code[0] + code[2])

edges: dict[str, set] = dict()

for c1, c2 in pairs:
    if not c1 in edges:
        edges[c1] = set()
    edges[c1].add(c2)

CODE = []

for digit in digits:
    if not digit in edges:
        CODE.append(digit)

while len(CODE) < len(digits):
    for digit in edges:
        if digit in CODE:
            continue
        if edges[digit] == set(CODE):
            CODE.append(digit)

print(''.join(reversed(CODE)))
