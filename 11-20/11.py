table = []

with open('11.txt', 'r') as fi:
    for line in fi:
        table.append(list(map(int, line.split(' '))))

N = 20

max_product = 0

def get_max_product(row, length=N):
    if length < 4:
        product = 1
        for i in range(length):
            product *= row[i]
        return product

    max_product = 0

    product = row[0] * row[1] * row[2] * row[3]
    if product > max_product:
        max_product = product

    for x in range(4, length):
        if row[x - 4] != 0:
            product = (product // row[x - 4]) * row[x]
        else:
            product = row[x] * row[x - 1] * row[x - 2] * row[x - 3]
        if product > max_product:
            max_product = product
    
    return max_product

# Lines and columns

for i in range(N):
    row = table[i]
    product = get_max_product(row)
    if product > max_product:
        max_product = product

    col = [table[y][i] for y in range(N)]
    product = get_max_product(col)
    if product > max_product:
        max_product = product

# Diagonals

for t in range(2 * N - 1):
    diag1 = [table[x][t - x] for x in range(N) if N > t - x >= 0]
    product = get_max_product(diag1, length=len(diag1))
    if product > max_product:
        max_product = product

    diag2 = [table[x][t - N + 1 + x] for x in range(N) if N > t - N + 1 + x >= 0]
    product = get_max_product(diag2, length=len(diag2))
    if product > max_product:
        max_product = product

print(max_product)
