LIMIT = 1000

# Method 1 : generate triplets

def multiply(R, v):
    return [R[i][0] * v[0] + R[i][1] * v[1] + R[i][2] * v[2] for i in range(3)]

R1 = ((1, -2, 2), (2, -1, 2), (2, -2, 3))
R2 = ((1, 2, 2), (2, 1, 2), (2, 2, 3))
R3 = ((-1, 2, 2), (-2, 1, 2), (-2, 2, 3))

V = [3, 4, 5]

def generate_triplets(v):
    if sum(v) > LIMIT:
        return []

    return [v] + generate_triplets(multiply(R1, v)) + generate_triplets(multiply(R2, v)) + generate_triplets(multiply(R3, v))

triplets = generate_triplets(V)

perimeters = [0 for _ in range(LIMIT + 1)]

for triplet in triplets:
    s = sum(triplet)
    for k in range(1, LIMIT // s + 1):
        perimeters[s * k] += 1

print(max(range(LIMIT + 1), key=lambda i:perimeters[i]))

# Method 2 : exhaustive search (SLOW : 44s)

max_count = 0
max_p = None

for p in range(3 + 4 + 5, LIMIT + 1):
    count = 0
    for a in range(1, p - 1):
        for b in range(a, p - 1):
            c = p - a - b
            if a * a + b * b == c * c:
                count += 1

    if count > max_count:
        max_count = count
        max_p = p

print(max_p)

