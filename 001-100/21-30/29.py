numbers = set()

for a in range(2, 100 + 1):
    for b in range(2, 100 + 1):
        numbers.add(a ** b)

print(len(numbers))
