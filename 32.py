# a * b = c
# Only need to check a and b with 1 and 4 or 2 and 4 digits
# No need to check any number containing a 0
# Only need to check a < b

products = set()

def is_pandigital(a, b, c):
    digits = [*str(a), *str(b), *str(c)]
    digits.sort()
    return digits == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

two_digits_to_check = [n for n in range(10, 100) if not '0' in str(n)]
three_digits_to_check = [n for n in range(100, 1000) if not '0' in str(n)]
four_digits_to_check = [n for n in range(1000, 10000) if not '0' in str(n)]

for a in range(1, 10):
    for b in four_digits_to_check:
        c = a * b
        if is_pandigital(a, b, c):
            products.add(c)


for a in two_digits_to_check:
    for b in three_digits_to_check:
        c = a * b
        if is_pandigital(a, b, c):
            products.add(c)


print(sum(products))
