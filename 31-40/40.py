LIMIT = 1_000_000

champernowne = []

n = 1
while len(champernowne) < LIMIT:
    champernowne.extend(str(n))
    n += 1

product = 1
for power in range(7):
    product *= int(champernowne[10**power - 1])

print(product)
