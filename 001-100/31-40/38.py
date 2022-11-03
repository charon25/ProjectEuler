n = 0

largest_pandigital = '000000000'

DIGITS = [str(k) for k in range(1, 10)]

# Cannot be over 10000 as len(str(n) + str(2 * n)) > 9
for n in range(10000):
    k = 1
    concat = ''
    while len(concat) < 9:
        concat += str(n * k)
        k += 1
    if len(concat) == 9 and list(sorted(concat)) == DIGITS:
        if concat > largest_pandigital:
            largest_pandigital = concat

print(largest_pandigital)
