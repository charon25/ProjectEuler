from math import gcd

def simplify_fraction(num, denom):
    g = gcd(num, denom)
    return (num // g, denom // g)

fractions = []

for num in range(10, 100):
    for denom in range(num + 1, 100):
        if num % 10 == 0 and denom % 10 == 0:
            continue
        intersection = set(str(num)).intersection(str(denom))
        if len(intersection) != 1:
            continue
        digit = intersection.pop()
        new_num = str(num).replace(digit, '')
        new_denom = str(denom).replace(digit, '')
        new_num = int(new_num) if new_num else int(digit)
        new_denom = int(new_denom) if new_denom else int(digit)
        if simplify_fraction(num, denom) == simplify_fraction(new_num, new_denom):
            fractions.append((num, denom))

prod_num = 1
prod_denom = 1

for num, denom in fractions:
    prod_num *= num
    prod_denom *= denom

print(simplify_fraction(prod_num, prod_denom)[1])
