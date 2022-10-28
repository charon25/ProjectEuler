LIMIT = 1_500_000

def multiply(R, v):
    return [R[i][0] * v[0] + R[i][1] * v[1] + R[i][2] * v[2] for i in range(3)]

R1 = ((1, -2, 2), (2, -1, 2), (2, -2, 3))
R2 = ((1, 2, 2), (2, 1, 2), (2, 2, 3))
R3 = ((-1, 2, 2), (-2, 1, 2), (-2, 2, 3))

V = [3, 4, 5]

def generate_unique_triplets(v):
    if sum(v) > LIMIT:
        return []

    return [v] + generate_unique_triplets(multiply(R1, v)) + generate_unique_triplets(multiply(R2, v)) + generate_unique_triplets(multiply(R3, v))

triplets = generate_unique_triplets(V)

count = {}

for triplet in triplets:
    L = sum(triplet)

    for kL in range(L, LIMIT + 1, L):
        if not kL in count:
            count[kL] = 0
        count[kL] += 1

print(len([1 for L in count if count[L] == 1]))
